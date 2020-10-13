from flask import render_template, flash, redirect, url_for, make_response, session, request
from app import app
from app.forms import LoginForm,RegisterForm,AdminForm,EditItem,EditProfileForm,EditUserForm,EditAdminForm,RegisterAdminForm
from app.backend import getProfile,loginUser,registerUser,editProfile,adminUser,listItems,listUsers,getProduct,getUser,updateProduct,updateUser,deleteUser,listAdmins, deleteAdmin,updateAdmin,getAdmin,registerAdmin

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
            session['cart'] = {}
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
       print("this is the userid {}".format(userid))
       username,email,about = getProfile(userid)
    return render_template('profile.html', username=username, email = email, about=about)

#Editing Profile Page
@app.route('/editProfile', methods=['GET','POST'])
def edit_profile():
    form = EditProfileForm()
    userid = session.get('userid')
    username, email, about = getProfile(userid)
    if form.validate_on_submit():
        username = form.username.data
        about = form.about.data
        reply = editProfile(username,about,userid)
        if reply [0] == True:
            flash('Your changes have been saved.')
            return redirect(url_for('profile'))
        else:
            flash("Username or email already in use! Try again.")
            return redirect(url_for('edit_profile'))
    elif request.method == 'GET':
        form.username.data = username
        form.about.data = about
    return render_template('editProfile.html', title='Edit Profile',form=form)

# Logout
@app.route('/logout')
def logout():
    session.pop('loggedin',None)
    session.pop('userid',None)
    session.pop('username',None)
    session.pop('admin',None)
    session.pop('cart',None)
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
            session['cart'] = {}
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
@app.route("/categ ory/<category>")
def catPg(category):
    listings = getRelated(category)
    results = []
    for item in listings:
        item = list(item)
        results.append(item)
    return render_template('category.html', category = category, listings=results, empty=False)        


# Product Page
@app.route('/product/<int:id>')
def prodPg(id):
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
            session['cart'] = {}
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
        info = [productid,form.productName.data,form.productPrice.data,form.productDesc.data,form.productCat.data]
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
            form.productCat.data = data[4]
    return render_template('edititem.html', title='Edit Item', form = form)

# Admin Add Item
@app.route('/additem', methods=['GET', 'POST'])
def additem():
    if session.get('admin') != True:
        return redirect(url_for('index'))
    form = AddItem()
    if form.validate_on_submit():
        info = [form.productName.data,form.productPrice.data,form.productDesc.data,form.productCat.data]
        if addProduct(info) == False:
            flash("Item addition failed. Try again")
        else:
            flash("Item Added Successfully!")
        return redirect(url_for('manageitem'))
    return render_template('additem.html', title='Add New Item', form = form)

# Admin Manage Users
@app.route('/manageuser', methods=['GET', 'POST'])
def manageuser():
    if session.get('admin') != True:
        return redirect(url_for('index'))
    data = listUsers()
    return render_template('manageuser.html', title='Manage Users', data = data)

#Admin Edit User
@app.route('/edituser', methods=['GET','POST'])
def edituser():
    if session.get('admin') != True:
        return redirect(url_for('index'))
    form = EditUserForm()
    userid = request.args.get('userid')
    if form.validate_on_submit():
        info = [userid,form.username.data,form.email.data,form.about.data]
        print(info)
        if updateUser(info) == False:
            flash("User update failed. Please try again.")
        else:
            flash("Updated Successfully!")
        return redirect(url_for("manageuser"))
    elif request.method =="GET":
        data = getUser(userid)
        if data == False:
            print(data)
            return render_template('editUser.html', title="Edit User",form=form)
        else:
            form.username.data = data[0]
            form.email.data = data[1]
            form.about.data = data[2]
    return render_template('editUser.html', title='Edit User', form = form)

@app.route('/deleteuser', methods=['GET', 'POST','DELETE'])
def deleteuser():
    if session.get('admin') != True:
        return redirect(url_for('index'))
    userid = request.args.get('userid')
    data = deleteUser(userid)
    if data == False:
        flash("Fail to delete please try again.")
    else:
        flash("Deleted successfully")
    return redirect(url_for("manageuser"))

@app.route('/addUser', methods=['GET','POST'])
def adduser():
    if session.get('admin') != True:
        return redirect(url_for('index'))    
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        email = form.email.data
        reply = registerUser(username,password,email)
        if reply[0] == True:
            flash("Successfully added new user")
            return redirect(url_for('manageuser'))
        else:
            flash("Username or email already in use! Try again.")
            return redirect(url_for('manageuser'))
    elif request.method == "GET":
        return render_template('adduser.html',form = form)
    return render_template('adduser.html',form = form)

# Admin Manage Admins
@app.route('/manageadmin', methods=['GET', 'POST'])
def manageadmin():
    if session.get('admin') != True:
        return redirect(url_for('index'))
    data = listAdmins()
    return render_template('manageadmin.html', data = data)

#Admin Delete Admin
@app.route('/deleteadmin', methods=['GET', 'POST','DELETE'])
def deleteadmin():
    if session.get('admin') != True:
        return redirect(url_for('index'))
    adminid = request.args.get('adminid')
    data = deleteAdmin(adminid)
    if data == False:
        flash("Fail to delete please try again.")
    else:
        flash("Deleted successfully")
    return redirect(url_for("manageadmin"))

@app.route('/editadmin', methods=['GET','POST'])
def editadmin():
    if session.get('admin') != True:
        return redirect(url_for('index'))
    form = EditAdminForm()
    adminid = request.args.get('adminid')
    if form.validate_on_submit():
        info = [adminid,form.username.data]
        print(info)
        if updateAdmin(info) == False:
            flash("User update failed. Please try again.")
        else:
            flash("Updated Successfully!")
        return redirect(url_for("manageadmin"))
    elif request.method =="GET":
        data = getAdmin(adminid)
        if data == False:
            print(data)
            return render_template('editAdmin.html', title="Edit User",form=form)
        else:
            form.username.data = data[0]
    return render_template('editAdmin.html', title='Edit User', form = form)

@app.route('/addAdmin', methods=['GET','POST'])
def addadmin():
    if session.get('admin') != True:
        return redirect(url_for('index'))    
    form = RegisterAdminForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        reply = registerAdmin(username,password)
        if reply[0] == True:
            flash("Successfully added new user")
            return redirect(url_for('manageadmin'))
        else:
            flash("Username already in use! Try again.")
            return redirect(url_for('manageadmin'))
    elif request.method == "GET":
        return render_template('addadmin.html',form = form)
    return render_template('addadmin.html',form = form)
# Adding Item to Cart
@app.route('/addcart', methods=['POST'])
def addcart():
    productid = request.values.get('productid')
    quantity = request.values.get('quantity')
    session['cart'][productid] = quantity
    session.modified = True
    flash("Item added to cart successfully!")
    return redirect(url_for('index'))

# Test Page
@app.route('/testPage')
def testPage():
    testinfo = test()
    return render_template('test.html', test = testinfo)
