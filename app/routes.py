from flask import render_template, flash, redirect, url_for, make_response, session, request
from app import app
from app.forms import *
from app.backend import *

# Index Page
@app.route('/')
def home():
    allListings = listItems()
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
    if session.get('loggedin') != True:
        return redirect(url_for('login'))
    allListings = listItems()
    listings = []
    for item in allListings:
        item = list(item)
        if len(listings) < 4:
            listings.append(item)
        else:
            break
    return render_template('index.html', listings = listings)

# Login Page
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        reply = loginUser(username,password)
        if reply[0] == True:
            session['cart'] = {}
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
    if session.get('loggedin') == False:
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

# search results
@app.route('/search', methods = ['POST'])
def search():
    query = request.form['search']
    emptyCheck = query.replace(' ','')
    if emptyCheck == '':
        return render_template('search.html', query = "blank", listings=[], empty=True)
    else:
        listings = listItems()
        results = []
        for item in listings:
            item = list(item)
            if query in item[1]:
                results.append(item)
        return render_template('search.html', query = query, listings=results, empty=False)        
# Category Page
@app.route("/category/<category>")
def catPg(category):
    listings = getRelated(category)
    results = []
    for item in listings:
        item = list(item)
        results.append(item)
    return render_template('category.html', category = category, listings=results, empty=False)        


# Product Page
@app.route('/product/<int:id>', methods=["GET","POST"])
def prodPg(id):
    if request.method == 'POST':
        quantity = int(request.form["quantity"])
        
        print(str(id))
        if str(id) in session.get('cart'):
            session['cart'][str(id)] += quantity
            print('increment')
        else:
            session['cart'][str(id)] = quantity
            print('new')
        print(session.get('cart')[str(id)])
        cart = session.get('cart')
        print(cart)
        session.modified = True
        flash("Item added to cart successfully!")
        return(redirect('/index'))
    else:
        details = getProduct(id)
        colors = list(getColors(id))
        color = []
        sizes = list(getSizes(id))
        size = []
        for i in colors:
            if (str(i) == "(None,)") or (str(i) == "('',)"):
                continue
            else:
                i = str(i)
                i = i[2:-3]
                if i not in color:
                    color.append(i)

        for i in sizes:
            if (str(i) == "(None,)") or (str(i) == "('',)"):
                continue
            else:
                a = str(i)[2:-3]
                if a not in size:
                    size.append(a)

        info = list(details)
        related = getRelated(info[4])
        listings = []
        if related == False:
            return render_template('product.html', info = info, sizes = size, colors = color)
        else:
            for item in related:
                item = list(item)
                if len(listings) < 4:
                    listings.append(item)
                else:
                    break
            return render_template('product.html', info = info, sizes = size, colors = color, listings=listings)



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

