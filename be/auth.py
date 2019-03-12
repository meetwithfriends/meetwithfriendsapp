from flask import Flask, jsonify, make_response, request
import uuid
import datetime
import time
import ConnectionUtils
import Constants
import hashlib
import markdown
import jwt

app = Flask(__name__)
app.config['SECRET'] = Constants.secret_key
connection = ConnectionUtils.connection()
while True:
    connection = ConnectionUtils.connection()
    if connection:
        break
    print("Waiting 10s for reconnect...")
    time.sleep(10)



def get_user_by_token(token):
    cur = connection.cursor()
    cur.execute("select user_id from sessions where token=%s and due_date < %s < start_date",
                (token, datetime.datetime.utcnow()))
    try:
        user_id = cur.fetchone()
        return user_id[0]
    except:
        return ''


def get_user_by_email(email):
    cur = connection.cursor()
    cur.execute("select id from users where email=%s", (email, ))
    try:
        user_id = cur.fetchone()
        return user_id[0]
    except:
        return ''


def get_user_name_by_id(id):
    cur = connection.cursor()
    cur.execute("select first_name + ' ' + last_name from users where id=%s", (id, ))
    try:
        user_id = cur.fetchone()
        return user_id[0]
    except:
        return ''


def get_group_name_by_id(id):
    cur = connection.cursor()
    cur.execute("select name from groups where id=%s", (id, ))
    try:
        group_name = cur.fetchone()
        return group_name[0]
    except:
        return ''


@app.route('/')
def get_api_calls_list():
    with open('README.md', 'r') as md_file:
        readme = md_file.read()
        return markdown.markdown(readme)


@app.after_request
def allow_cross_domain(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'content-type'
    return response


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

@app.route('/logout', methods=['POST'])
def logout():
    user_id = get_user_by_token(request.headers.get('token'))

    if not user_id:
        return make_response(jsonify({'message': 'You should be logged in to perform this action'}), 401)

    cur = connection.cursor()
    delete_sql = "delete from sessions where user_id=%s"
    cur.execute(delete_sql, (user_id, ))
    connection.commit()

    return make_response(jsonify({'message': 'You have been successfully logged out.'}), 200)

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
    cur.execute("Insert into groups (id, name, note, avatar, creator_id) values (%s, %s, %s, %s, %s)",
                (group_id, req['name'], req['note'], req['avatar'], user_id))
    cur.execute("Insert into users_in_groups (id, user_id, group_id, is_admin) values (%s, %s, %s, %s)",
                (str(uuid.uuid4()), user_id, group_id, True))
    try:
        connection.commit()
        return make_response(jsonify(
            {'id': group_id, 'name': req['name'], 'note': req['note'], 'avatar': req['avatar'],
             'creator_id': user_id}), 200)
    except:
        return make_response(jsonify({'message': 'Internal server error'}), 500)


@app.route('/place', methods=['post'])
def create_new_place():
    user_id = get_user_by_token(request.headers.get('token'))
    if not user_id:
        return make_response(jsonify({'message': 'You should be logged in to perform this action'}), 401)
    #todo: add check on group rights
    req = request.get_json()
    cur = connection.cursor()
    
    place_id = str(uuid.uuid4())
    cur.execute("Insert into places (id, name, address, site, group_id) values (%s, %s, %s, %s, %s)",
                (place_id, req['name'], req['address'], req['site'], req['group_id']))
    try:
        connection.commit()
        return make_response(jsonify(
            {'id': place_id, 'name': req['name'], 'address': req['address'], 'site': req['site'],
             'group_id': req['group_id']}), 200)
    except:
        return make_response(jsonify({'message': 'Internal server error'}), 500)


@app.route('/places/<group_id>', methods=['GET'])
def get_group_places(group_id):
    user_id = get_user_by_token(request.headers.get('token'))
    if not user_id:
        return make_response(jsonify({'message': 'You should be logged in to perform this action'}), 401)
    #todo: add check on group rights
    cur = connection.cursor()
    cur.execute("SELECT * FROM places where group_id=%s", (group_id,))
    row_headers = [x[0] for x in cur.description]
    places = cur.fetchall()
    json_data = []
    for result in places:
        json_data.append(dict(zip(row_headers, result)))
    return jsonify(json_data)


@app.route('/meal_provider', methods=['post'])
def create_new_meal_provider():
    user_id = get_user_by_token(request.headers.get('token'))
    if not user_id:
        return make_response(jsonify({'message': 'You should be logged in to perform this action'}), 401)
    #todo: add check on group rights
    req = request.get_json()
    cur = connection.cursor()
    
    provider_id = str(uuid.uuid4())
    cur.execute("Insert into meal_providers (id, name, address, site, group_id, note) values (%s, %s, %s, %s, %s, %s)",
                (provider_id, req['name'], req['address'], req['site'], req['group_id'], req['note']))
    try:
        connection.commit()
        return make_response(jsonify(
            {'id': provider_id, 'name': req['name'], 'address': req['address'], 'site': req['site'],
             'group_id': req['group_id'], 'note': req['note']}), 200)
    except:
        return make_response(jsonify({'message': 'Internal server error'}), 500)


@app.route('/meal_providers/<group_id>', methods=['GET'])
def get_group_meal_providers(group_id):
    user_id = get_user_by_token(request.headers.get('token'))
    if not user_id:
        return make_response(jsonify({'message': 'You should be logged in to perform this action'}), 401)
    #todo: add check on group rights
    cur = connection.cursor()
    cur.execute("SELECT * FROM meal_providers where group_id=%s", (group_id,))
    row_headers = [x[0] for x in cur.description]
    places = cur.fetchall()
    json_data = []
    for result in places:
        json_data.append(dict(zip(row_headers, result)))
    return jsonify(json_data)


@app.route('/meal', methods=['post'])
def create_new_meal():
    user_id = get_user_by_token(request.headers.get('token'))
    if not user_id:
        return make_response(jsonify({'message': 'You should be logged in to perform this action'}), 401)
    #todo: add check on group rights
    req = request.get_json()
    cur = connection.cursor()
    
    meal_id = str(uuid.uuid4())
    cur.execute("Insert into meals (id, name, provider_id, image) values (%s, %s, %s, %s)",
                (meal_id, req['name'], req['provider_id'], req['image']))

    #todo: add error handling for nullable fields
    try:
        connection.commit()
        return make_response(jsonify(
            {'id': meal_id, 'name': req['name'], 'provider_id': req['provider_id'], 'image': req['image']}), 200)
    except:
        return make_response(jsonify({'message': 'Internal server error'}), 500)


@app.route('/meals/<group_id>', methods=['GET'])
def get_group_meals(group_id):
    user_id = get_user_by_token(request.headers.get('token'))
    if not user_id:
        return make_response(jsonify({'message': 'You should be logged in to perform this action'}), 401)
    #todo: add check on group rights
    cur = connection.cursor()
    cur.execute("SELECT m.* FROM meals m, meal_providers p where m.provider_id = p.id and p.group_id=%s", (group_id,))
    row_headers = [x[0] for x in cur.description]
    places = cur.fetchall()
    json_data = []
    for result in places:
        json_data.append(dict(zip(row_headers, result)))
    return jsonify(json_data)


@app.route('/invitations', methods=['GET'])
def get_user_invitations():
    user_id = get_user_by_token(request.headers.get('token'))
    if not user_id:
        return make_response(jsonify({'message': 'You should be logged in to perform this action'}), 401)

    cur = connection.cursor()
    cur.execute("SELECT * FROM invitations WHERE invitee_id = %s", (user_id,))
    row_headers = [x[0] for x in cur.description]
    invitations = cur.fetchall()
    json_data = []
    for result in invitations:
        json_data.append(dict(zip(row_headers, result)))
    return jsonify(json_data)


@app.route('/invitation', methods=['POST'])
def invite_user_to_group():
    user_id = get_user_by_token(request.headers.get('token'))
    if not user_id:
        return make_response(jsonify({'message': 'You should be logged in to perform this action'}), 401)
    req = request.get_json()
    cur = connection.cursor()
    invitation_id = str(uuid.uuid4())
    invitee_id = get_user_by_email(req['email'])
    user_name = get_user_name_by_id(user_id)
    group_name = get_group_name_by_id(req['group_id'])
    cur.execute("Insert into invitations (id, invitee_id, group_name, group_id, invitator_id, invitator_name, message) values (%s, %s, %s, %s, %s, %s, %s)",
        (invitation_id, invitee_id, group_name, req['group_id'], user_id, user_name, req['message']))
    try:
        connection.commit()
        return make_response(jsonify(
            {'id': invitation_id, 'invitee_email': req['email'], 'group_name': group_name, 'group_id': req['group_id'], 'message': req['message']}), 200)
    except:
        return make_response(jsonify({'message': 'Internal server error'}), 500)


@app.route('/accept_invitation', methods=['POST'])
def accept_group_invitation():
    user_id = get_user_by_token(request.headers.get('token'))
    if not user_id:
        return make_response(jsonify({'message': 'You should be logged in to perform this action'}), 401)
    req = request.get_json()
    cur = connection.cursor()

    cur.execute("select 1 from invitations where id=%s and invitee_id=%s and group_id=%s", (req['invitation_id'], user_id, req['group_id']))
    if not cur.fetchone():
        return make_response(jsonify({'message': 'You are not invited to this group'}), 403)

    cur.execute("Insert into users_in_groups (id, user_id, group_id, is_admin) values (%s, %s, %s, %s)",
                (str(uuid.uuid4()), user_id, req['group_id'], True))
    cur.execute("delete from invitations where id=%s", (req['invitation_id'], ))
    try:
        connection.commit()    
        return make_response(jsonify({'message': 'Successfully joined the group'}), 200)
    except:
        return make_response(jsonify({'message': 'Internal server error'}), 500)
