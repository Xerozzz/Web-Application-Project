from app import app, conn
from werkzeug.security import generate_password_hash, check_password_hash

# Test Function
def test():
    username = 'Xeroz'
    sql = "SELECT * FROM users where username = '{}'".format(username)
    cursor = conn.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    cursor.close()
    return data

# Add User
def addUser():
    print("Test")

# Login Required
def loginRequired(session):
    if session:
        return True
    else:
        return False

# Login User
def loginUser(username,password):
    sql = "SELECT * FROM users WHERE username = '{}'".format(username)
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()[0]
        cursor.close()
        if username == data[1] and check_password_hash(data[2],password):
            return [True,data[0]]
        else:
            return [False,0]
    except:
        return [False,0]

# Register user
def registerUser(username,password,email):
    hash = generate_password_hash(password)
    sql = "INSERT INTO users (username,hash,email) VALUES ('{0}','{1}','{2}')".format(username,hash,email)
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        data = cursor.lastrowid
        cursor.close()
        print(data)
        return [True, data]
    except:
        return[False,0]