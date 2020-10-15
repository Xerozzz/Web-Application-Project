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

# Get user profile
def getProfile(userid):
    sql = "SELECT username, email, about FROM users WHERE userid = '{}'".format(userid)
    conn.connect()
    cursor = conn.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    for row in data:
        username = row[0]
        email = row[1]
        about = row [2]
    cursor.close()
    conn.close()
    print(username,email,about)
    return username,email,about
    
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

# Register Admin
def registerAdmin(username,password):
    hash = generate_password_hash(password)
    sql = "INSERT INTO admin (username,hash) VALUES ('{0}','{1}')".format(username,hash)
    try:
        conn.connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        data = cursor.lastrowid
        cursor.close()
        conn.close()
        print(data)
        return [True, data]
    except:
        return[False,0]

# Edit user profile
def editProfile(username,email,userid):
    print(username,email,userid)
    query = ''' UPDATE users SET username = %s, email =%s WHERE userid =%s '''
    data = (username,email,userid)
    try:
        conn.connect()
        cursor = conn.cursor()
        cursor.execute(query,data)
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

# List Products
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

# List users
def listUsers():
    sql = 'SELECT userid, username,email,about FROM users'
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

# List users
def listAdmins():
    sql = 'SELECT adminid, username FROM admin'
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


# Get Specific Product
def getProduct(productid):
    sql = "SELECT * FROM products WHERE productid = '{}'".format(productid)
    try:
        conn.connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()[0]
        cursor.close()
        conn.close()
        return data
    except:
        return False

# Get Specific User
def getUser(userid):
    sql = "SELECT username,email,about FROM users WHERE userid = '{}'".format(userid)
    try:
        conn.connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()[0]
        cursor.close()
        conn.close()
        return data
    except:
        return False

# Get products of same category
def getRelated(category):
    sql = "SELECT * FROM products WHERE category = '{}'".format(category)
    try:
        conn.connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        return data
    except:
        return False

# Get Specifc Admin
def getAdmin(adminid):
    sql = "SELECT username FROM admin WHERE adminid = '{}'".format(adminid)
    try:
        conn.connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()[0]
        cursor.close()
        conn.close()
        return data
    except:
        return False


# Get sizes
def getSizes(productid):
    sql = "SELECT size FROM variations WHERE productid = {}".format(productid)
    try:
        conn.connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        return data
    except:
        return False


# Get colors
def getColors(productid):
    sql = "SELECT color FROM variations WHERE productid = {}".format(productid)
    try:
        conn.connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        return data
    except:
        return False

# Update Product
def updateProduct(info):
    sql = "UPDATE products SET name = '{1}', price = {2}, description = '{3}', category = '{4}' where productid = {0}".format(info[0],info[1],info[2],info[3],info[4])
    try:
        conn.connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        data = cursor.rowcount
        cursor.close()
        conn.close()
        return data
    except:
        return False

# Add New Products
def addProduct(info):
    sql =  "INSERT INTO products (name,price,description,category) VALUES ('{0}',{1},'{2}','{3}')".format(info[0],info[1],info[2],info[3])
    try: 
        conn.connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        data = cursor.rowcount
        cursor.close()
        conn.close()
        print(data)
        return data
    except:
        return False

def updateUser(info):
    sql = "UPDATE users SET username='{1}', email='{2}', about='{3}' where userid='{0}'".format(info[0],info[1],info[2],info[3])
    try:
        conn.connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        data = cursor.rowcount
        cursor.close()
        conn.close()
        print(data)
        return data
    except:
        return False


def updateAdmin(info):
    sql = "UPDATE admin SET username='{1}' where adminid='{0}'".format(info[0],info[1])
    try:
        conn.connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        data = cursor.rowcount
        cursor.close()
        conn.close()
        print(data)
        return data
    except:
        return False

def deleteUser(userid):
    sql = "DELETE FROM users WHERE userid = '{}'".format(userid)
    try:
        conn.connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        data = cursor.rowcount
        cursor.close()
        conn.close()
        return data
    except:
        return False

def deleteAdmin(adminid):
    sql = "DELETE FROM admin WHERE adminid = '{}'".format(adminid)
    try:
        conn.connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        data = cursor.rowcount
        cursor.close()
        conn.close()
        return data
    except:
        return False