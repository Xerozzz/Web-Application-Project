from flask import render_template, flash, redirect, url_for,make_response, session, request
from app import app, conn
from app.forms import LoginForm, RegisterForm
from app.backend import *

# Index Page
@app.route('/')
def home():
    allListings = allProds()
    listings = []
    for item in allListings:
        item = list(item)
        if len(listings) < 4:
            listings.append(item)
        else:
            break
    return render_template('index.html', listings = listings)

@app.route('/index')
def index():
    if loginRequired(session.get('loggedin')) == False:
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

# search results
@app.route('/search', methods = ['POST'])
def search():
    query = request.form['search']
    emptyCheck = query.replace(' ','')
    if emptyCheck == '':
        return render_template('search.html', query = "blank", listings=[], empty=True)
    else:
        listings = allProds()
        print(listings)
        results = []
        for item in listings:
            item = list(item)
            if query in item[1]:
                results.append(item)
        return render_template('search.html', query = query, listings=results, empty=False)        


# Test Page
@app.route('/testPage')
def testPage():
    testinfo = test()
    return render_template('test.html', test = testinfo)