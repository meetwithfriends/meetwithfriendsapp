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
    sql = "SELECT passhash FROM Users WHERE email = %s"
    cur.execute(sql, (auth['email'],))
    stored_hash = cur.fetchone()
    pass_hash = hashlib.sha256()
    pass_hash.update(auth['pass'].encode('utf-8'))

    if stored_hash[0] != str(pass_hash.hexdigest()):
        return make_response(jsonify({'message': 'Username or password incorrect'}), 401)

    token = jwt.encode({'email': auth['email'], 'expies_at': str(datetime.datetime.utcnow() + datetime.timedelta(hours=48))},
                       app.config['SECRET'])
    return make_response(jsonify({'email': auth['email'], 'token': token.decode('UTF-8')}), 200)


@app.route('/signup', methods=['POST'])
def sign_up():
    req = request.get_json()
    pass_hash = hashlib.sha256()
    pass_hash.update(req['pass'].encode('utf-8'))
    cur = connection.cursor()
    sql = "insert into Users (Id, email, passhash) values (%s, %s, %s)"
    cur.execute(sql, (str(uuid.uuid4()), req['email'], str(pass_hash.hexdigest())))
    connection.commit()
    return make_response(jsonify({'message': 'User created successfully'}), 200)


if __name__ == '__main__':
    app.run(debug=True)

