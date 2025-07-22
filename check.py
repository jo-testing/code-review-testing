# def login(username, password):
#     query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
#     return db.execute(query).fetchone()

def login(username, password):
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    return db.execute(query).fetchone()