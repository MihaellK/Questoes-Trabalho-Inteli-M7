from flask import Flask, request, render_template, redirect, url_for, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash

import jwt

from database import create_table
from database import User, Note
from database import db as db
from auth import token_required

app = Flask(__name__)


app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:password@localhost:5432/postgres"
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///./test.db"
app.config['JWT_SECRET_KEY'] = "be7e1ac39b5a29e541c551a3ebb165c5"
app.config['JWT_ALGORITHM'] = 'HS256'
db.init_app(app)

# Tabelas
note_db = Note()
create_table(app)

@app.route('/')
@app.route('/index')
def index():
    return render_template('layout.html')

@app.route('/signup')
def signup():
    return render_template('/auth/signup.html')

# Cria um usuario 
@app.route('/add_user', methods=['POST'])
def add_user():
    name = request.form['name']
    password = request.form['password']
    
    if not User.query.filter_by(name=name).first():
    
        hash_password = generate_password_hash(password, method="pbkdf2")

        new_user = User(name=name, password=hash_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect("http://localhost:5000/") 
    else:
        return "Invalid Credentials", 401

@app.route('/login')
def login():
    # return render_template('/auth/login.html')
    name_login = request.form['name']
    password_login = request.form['password']

    user = User.query.filter_by(name=name_login).first()

    if user and check_password_hash(user.password, password_login):
        try:
            key = "be7e1ac39b5a29e541c551a3ebb165c5"
            user_token = jwt.encode({"user_id": str(user.id)}, key, algorithm="HS256")

            # Armazenar o token em um cookie seguro
            response = make_response(redirect(url_for('dashboard')))
            response.set_cookie('user_id', str(user.id), httponly=True, secure=True)
            response.set_cookie('auth_token', user_token, httponly=True, secure=True)  # httponly=True para proteção contra ataques XSS


            return response

        except Exception as e:
                return {
                    "error": "Something went wrong",
                    "message": str(e)
                }, 500
    else:
        return "Credenciais inválidas", 401

@app.route('/notes')
@token_required
def notes(user):
    jsonify(user)
    notes = Note.query.all()
    return render_template('notes.html', notes=notes)

# Adicionar nova nota
@app.route('/add_note', methods=['POST'])
def add_note():
    note_text = request.form['note_text']
        
    new_note = Note(note_text=note_text)
    db.session.add(new_note)
    db.session.commit()
    
    return redirect(url_for('notes'))

app.run(debug=True)