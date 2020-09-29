from app import app, conn
from werkzeug.security import generate_password_hash, check_password_hash

# DB Connection/Query Function for less code
def dbconn(query):
    cursor = conn.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    return data

# Test Function
def test():
    return dbconn("SELECT * FROM users")

# Add User
def addUser():
    print("Test")

# Login User
def loginUser(username):
    data = dbconn(f"SELECT * FROM users WHERE userid = {id}")
    return(data)