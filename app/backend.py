from app import app, conn
from werkzeug.security import generate_password_hash, check_password_hash

conn.close()
# Test Function
def test():
    username = 'Xeroz'
    sql = "SELECT * FROM users"
    conn.connect()
    cursor = conn.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return data

# Add User
def addUser():
    print("Test")
    
# Login User
def loginUser(username,password):
    sql = "SELECT * FROM users WHERE username = '{}'".format(username)
    try:
        conn.connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()[0]
        cursor.close()
        conn.close()
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
        conn.connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        data = cursor.lastrowid
        cursor.close()
        conn.close()
        return [True, data]
    except:
        return[False,0]

# Admin Login
def adminUser(username,password):
    sql = "SELECT * FROM admin WHERE username = '{}'".format(username)
    try:
        conn.connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()[0]
        cursor.close()
        conn.close()
        if username == data[1] and check_password_hash(data[2],password):
            return [True,data[0]]
        else:
            return [False,0]
    except:
        return [False,0]

# List Items
def listItems():
    sql = "SELECT * FROM products"
    try:
        conn.connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        return data
    except:
        return "An error has occurred, please check the backend"