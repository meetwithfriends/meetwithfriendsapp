from flask import Flask, jsonify, make_response, request
import uuid
import datetime
import ConnectionUtils
import Constants
import hashlib
import markdown
import jwt

app = Flask(__name__)
app.config['SECRET'] = Constants.secret_key
connection = ConnectionUtils.connection()


@app.route('/')
def get_api_calls_list():
    with open('README.md', 'r') as md_file:
        readme = md_file.read()
        return markdown.markdown(readme)


@app.route('/signin', methods=['POST'])
def sign_in():
    auth = request.get_json()

    if not auth or not auth['email'] or not auth['pass']:
        return make_response(jsonify({'message': 'Authorization required'}), 401)

    cur = connection.cursor()
    sql = "SELECT pass_hash, id FROM users WHERE email = %s"
    cur.execute(sql, (auth['email'],))
    stored_hash = cur.fetchone()

    pass_hash = hashlib.sha256()
    pass_hash.update(auth['pass'].encode('utf-8'))

    if stored_hash[0] != str(pass_hash.hexdigest()):
        return make_response(jsonify({'message': 'Username or password incorrect'}), 401)

    token_start_date = datetime.datetime.utcnow()
    token_due_date = token_start_date + datetime.timedelta(hours=48)
    token = jwt.encode(
        {'email': auth['email'], 'expies_at': str(token_due_date)}, app.config['SECRET'])

    delete_sql = "delete from sessions where user_id=%s"
    cur.execute(delete_sql, (stored_hash[1],))

    insert_sql = "INSERT INTO sessions (id, user_id, token, start_date, due_date) values (%s, %s, %s, %s, %s);"
    cur.execute(insert_sql,
                (str(uuid.uuid4()), stored_hash[1], token.decode('UTF-8'), str(token_start_date), str(token_due_date)))

    connection.commit()

    return make_response(jsonify({'email': auth['email'], 'token': token.decode('UTF-8')}), 200)

# TODO: add error handling
@app.route('/signup', methods=['POST'])
def sign_up():
    req = request.get_json()

    pass_hash = hashlib.sha256()
    pass_hash.update(req['pass'].encode('utf-8'))

    cur = connection.cursor()
    sql = "insert into users (id, email, pass_hash) values (%s, %s, %s);"

    cur.execute(sql, (str(uuid.uuid4()), req['email'], str(pass_hash.hexdigest())))
    connection.commit()

    return make_response(jsonify({'message': 'User created successfully'}), 200)


def get_user_by_token(token):
    cur = connection.cursor()
    cur.execute("select user_id from sessions where token=%s and due_date < %s < start_date",
                (token, datetime.datetime.utcnow()))
    try:
        user_id = cur.fetchone()
        return user_id[0]
    except:
        return ''


@app.route('/groups', methods=['GET'])
def get_user_groups():
    user_id = get_user_by_token(request.headers.get('token'))
    if not user_id:
        return make_response(jsonify({'message': 'You should be logged in to perform this action'}), 401)

    cur = connection.cursor()
    cur.execute("SELECT g.* FROM groups g, users_in_groups uig where uig.group_id = g.id and uig.user_id = %s", (user_id,))
    row_headers = [x[0] for x in cur.description]
    groups = cur.fetchall()
    json_data = []
    for result in groups:
        json_data.append(dict(zip(row_headers, result)))
    return jsonify(json_data)


@app.route('/group', methods=['post'])
def create_user_group():
    user_id = get_user_by_token(request.headers.get('token'))
    if not user_id:
        return make_response(jsonify({'message': 'You should be logged in to perform this action'}), 401)
    req = request.get_json()
    cur = connection.cursor()
    group_id = str(uuid.uuid4())
    print(group_id)
    print(req)
    cur.execute("Insert into groups (id, name, note, avatar, creator_id) values (%s, %s, %s, %s, %s)",
                (group_id, req['name'], req['note'], req['avatar'], user_id))
    cur.execute("Insert into users_in_groups (id, user_id, group_id, is_admin) values (%s, %s, %s, %s)",
                (str(uuid.uuid4()), user_id, group_id, True))
    try:
        connection.commit()
        return make_response(jsonify(
            {'group_id': group_id, 'name': req['name'], 'note': req['note'], 'avatar': req['avatar'],
             'creator_id': user_id}), 200)
    except:
        return make_response(jsonify({'message': 'Internal server error'}), 500)


@app.route('/place', methods=['post'])
def create_new_place():
    user_id = get_user_by_token(request.headers.get('token'))
    if not user_id:
        return make_response(jsonify({'message': 'You should be logged in to perform this action'}), 401)
    req = request.get_json()
    cur = connection.cursor()
    
    place_id = str(uuid.uuid4())
    cur.execute("Insert into places (id, name, address, site, group_id) values (%s, %s, %s, %s, %s)",
                (place_id, req['name'], req['address'], req['site'], req['group_id']))
    try:
        connection.commit()
        return make_response(jsonify(
            {'place_id': place_id, 'name': req['name'], 'address': req['address'], 'site': req['site'],
             'group_id': req['group_id']}), 200)
    except:
        return make_response(jsonify({'message': 'Internal server error'}), 500)


@app.route('/places/<group_id>', methods=['GET'])
def get_group_places(group_id):
    user_id = get_user_by_token(request.headers.get('token'))
    if not user_id:
        return make_response(jsonify({'message': 'You should be logged in to perform this action'}), 401)

    cur = connection.cursor()
    cur.execute("SELECT * FROM places where group_id=%s", (group_id,))
    row_headers = [x[0] for x in cur.description]
    places = cur.fetchall()
    json_data = []
    for result in places:
        json_data.append(dict(zip(row_headers, result)))
    return jsonify(json_data)


if __name__ == '__main__':
    app.run(debug=True)
