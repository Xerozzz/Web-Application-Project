from flask import render_template, flash, redirect, url_for, make_response, session, request
from app import app
from app.forms import *
from app.backend import *

# Index Page
@app.route('/')
@app.route('/index')
def index():
    if session.get('loggedin') != True:
        return redirect(url_for('login'))
    return render_template('index.html', title='Home')

# Login Page
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        reply = loginUser(username,password)
        if reply[0] == True:
            session['loggedin'] = True
            session['userid'] = reply[1]
            session['username'] = username
            return redirect(url_for('index'))
        else:
            flash("Invalid username or password")
            return redirect(url_for('login'))
    return render_template('login.html', title='Sign In', form=form)

# Logout
@app.route('/logout')
def logout():
    session.pop('loggedin',None)
    session.pop('userid',None)
    session.pop('username',None)
    session.pop('admin',None)
    return render_template('logout.html', title = "Log out")

# Register
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        email = form.email.data
        reply = registerUser(username,password,email)
        if reply[0] == True:
            session['loggedin'] = True
            session['userid'] = reply[1]
            session['username'] = username
            return redirect(url_for('index'))
        else:
            flash("Username or email already in use! Try again.")
            return redirect(url_for('register'))
    return render_template('register.html', title='Register', form=form)

# Admin Login
@app.route('/admin', methods=['GET', 'POST'])
def admin():
    form = AdminForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        reply = adminUser(username,password)
        if reply[0] == True:
            session['loggedin'] = True
            session['userid'] = reply[1]
            session['username'] = username
            session['admin'] = True
            return redirect(url_for('adminhome'))
        else:
            flash("Invalid username or password")
            return redirect(url_for('admin'))
    return render_template('admin.html', title='Admin Sign In', form=form)

# Admin Dashboard
@app.route('/adminhome', methods=['GET', 'POST'])
def adminhome():
    if session.get('admin') != True:
        return redirect(url_for('index'))
    return render_template('adminhome.html', title='Dashboard')

# Admin Manage Items
@app.route('/manageitem', methods=['GET', 'POST'])
def manageitem():
    if session.get('admin') != True:
        return redirect(url_for('index'))
    data = listItems()
    return render_template('manageitem.html', title='Manage Items', data = data)

# Admin Edit Item
@app.route('/edititem', methods=['GET', 'POST'])
def edititem():
    if session.get('admin') != True:
        return redirect(url_for('index'))
    form = EditItem()
    productid = request.args.get('productid')
    if form.validate_on_submit():
        info = [productid,form.productName.data,form.productPrice.data,form.productDesc.data]
        if updateProduct(info) == False:
            flash("Item update failed. Try again")
        else:
            flash("Updated Successfully!")
        return redirect(url_for('manageitem'))
    elif request.method == "GET":
        data = getProduct(productid)
        if data == False:
            return render_template('edititem.html', title='Edit Item', form = form)
        else:
            form.productName.data = data[1]
            form.productPrice.data = data[2]
            form.productDesc.data = data[3]
    return render_template('edititem.html', title='Edit Item', form = form)

# Admin Manage Users
@app.route('/manageuser', methods=['GET', 'POST'])
def manageuser():
    if session.get('admin') != True:
        return redirect(url_for('index'))
    return render_template('manageuser.html', title='Manage Users')

# Admin Manage Admins
@app.route('/manageadmin', methods=['GET', 'POST'])
def manageadmin():
    if session.get('admin') != True:
        return redirect(url_for('index'))
    return render_template('manageadmin.html', title='Manage Admin')

# Test Page
@app.route('/testPage')
def testPage():
    testinfo = test()
    return render_template('test.html', test = testinfo)