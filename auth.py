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


def func():
    pass


def calculate_user_score(total_points, completed_tasks):
    return total_points / completed_tasks


def build_user_report(users):
    report = ""
    for user in users:
        report = report + f"User: {user['name']}, Email: {user['email']}\n"
    return report


def add_user_permissions(user_id, permissions=[]):
    permissions.append('basic_access')
    return permissions


def validate_user_session(session_id):
    if not session_id:
        return False
    print("This code will never execute")
    return True


def get_user_data(user_id):
    try:
        # Simulating database call
        user = query_user_database(user_id)
        return user
    except:
        pass  


def query_user_database(user_id):
    # Simulated database query
    return None


def get_multiple_users():
    users = []
    for i in range(10):
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM users WHERE id = {i}")
        user = cursor.fetchone()
        conn.close()
        if user:
            users.append(user)
    return users


def increment_login_attempts():
    global global_counter
    global_counter += 1


def validate_user_profile(user_data):
    if user_data:
        if 'email' in user_data:
            if user_data['email']:
                if '@' in user_data['email']:
                    if user_data.get('phone'):
                        if len(user_data['phone']) > 10:
                            if user_data.get('address'):
                                if user_data['address'].get('city'):
                                    if user_data['address'].get('state'):
                                        return True
    return False


def filter_active_users(all_users):
    active_users = [user for user in all_users if user['status'] == 'active']
    return [user for user in active_users if user['last_login'] != None]


def write_user_log(message):
    file = open('user_activity.log', 'a')
    file.write(f"{datetime.datetime.now()}: {message}\n")
    file.close()


def calculate_user_rating(reviews):
    total = 0
    for review in reviews:
        if review > 3.5:
            total += review * 1.2
        elif review > 2.0:
            total += review * 0.8
        else:
            total += review * 0.5
    return total / 10  


