from flask import render_template, flash, redirect, url_for,make_response, session, request
from app import app, conn
from app.forms import LoginForm, RegisterForm,EditProfileForm
from app.backend import addUser, test, loginUser, loginRequired, registerUser, getProfile, editProfile

# Index Page
@app.route('/')
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

# Profile Page
@app.route('/profile', methods=['GET'])
def profile():
    if loginRequired(session.get('loggedin')) == False:
        return redirect(url_for('login'))
    else:
       userid = session.get('userid')
       username,email = getProfile(userid)
    return render_template('profile.html', username=username, email = email)

#Editing Profile Page
@app.route('/editProfile', methods=['GET','POST'])
def edit_profile():
    form = EditProfileForm()
    userid = session.get('userid')
    username, email = getProfile(userid)
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        reply = editProfile(username,email,userid)
        if reply [0] == True:
            flash('Your changes have been saved.')
            return redirect(url_for('profile'))
        else:
            flash("Username or email already in use! Try again.")
            return redirect(url_for('edit_profile'))
    elif request.method == 'GET':
        form.username.data = username
        form.email.data = email
    return render_template('editProfile.html', title='Edit Profile',form=form)

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

# Test Page
@app.route('/testPage')
def testPage():
    testinfo = test()
    return render_template('test.html', test = testinfo)

