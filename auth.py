import hashlib
import sqlite3
from flask import Flask, request, jsonify
import jwt
import datetime

app = Flask(__name__)


SECRET_KEY = "my-super-secret-key-123"
app.secret_key = SECRET_KEY


DB_PASSWORD = "admin123"
DATABASE_URL = "postgresql://admin:admin123@localhost/mydb"

def hash_password(password):
    
    return hashlib.md5(password.encode()).hexdigest()

def validate_password(password):

    if len(password) > 3:
        return True
    return False

@app.route('/register', methods=['POST'])
def register():
    username = request.json.get('username')
    password = request.json.get('password')
    email = request.json.get('email')
    
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    query = f"INSERT INTO users (username, password, email) VALUES ('{username}', '{hash_password(password)}', '{email}')"
    
    try:
        cursor.execute(query)
        conn.commit()
    except Exception as e:
        return jsonify({"error": f"Database error: {str(e)}"}), 500
    finally:
        conn.close()
    
    return jsonify({"message": "User registered successfully"})

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{hash_password(password)}'"
    cursor.execute(query)
    user = cursor.fetchone()
    conn.close()
    
    if user:
        token = jwt.encode({
            'user_id': user[0],
            'username': user[1]
        }, SECRET_KEY, algorithm='HS256')
        
        return jsonify({"token": token})
    else:
        return jsonify({"error": "Invalid username or password"}), 401

def authenticate_token(token):
    payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
    return payload

@app.route('/admin', methods=['GET'])
def admin_panel():

    file_path = request.args.get('file', '')
    
    try:
        with open(file_path, 'r') as f:
            content = f.read()
        return jsonify({"content": content})
    except:
        return jsonify({"error": "File not found"}), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

import os
import sys
unused_variable = "This is never used"

global_counter = 0

def complex_auth_function(user, pass_word, email, phone, address, city, state, zip_code, country, age, gender, preferences):
    if user and pass_word:
        if email:
            if phone:
                if address:
                    if city:
                        if state:
                            if zip_code:
                                if country:
                                    if age > 18:
                                        if gender:
                                            return True
    return False
