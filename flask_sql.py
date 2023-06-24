from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(75), nullable=False)
    email = db.Column(db.String(75), nullable=False)

    def __repr__(self):
        return f'<User {self.name}>'


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        new_user = User(name=name, email=email)
        db.session.add(new_user)
        db.session.commit()

    users = User.query.all()
    return render_template('index.html', users=users)

@app.route('/list_names', methods=['GET'])
def list_names():
    users = User.query.all()
    names = [user.name for user in users]
    # return render_template('names.html', names=names)
    return jsonify(names)

@app.route('/insert_users_json', methods=['POST'])
def create_user_json():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')

    if not name or not email:
        return jsonify({'error': 'Name and email are required.'}), 400

    new_user = User(name=name, email=email)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User created successfully.'}), 201

@app.route('/insert_users', methods=['POST'])
def create_user():
    name = request.args.get('name')
    email = request.args.get('email')

    if not name or not email:
        return jsonify({'error': 'Name and email are required.'}), 400

    new_user = User(name=name, email=email)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User created successfully.'}), 201

if __name__ == '__main__':
    app.run(debug=True)
