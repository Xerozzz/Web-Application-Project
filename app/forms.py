from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, HiddenField, IntegerField, FloatField, DecimalField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length

# Login Form
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')

# Register Form
class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Register')

# Admin Form
class AdminForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')

# Edit Item Form
class EditItem(FlaskForm):
    productName = StringField('Product Name', validators=[DataRequired()])
    productPrice = DecimalField('Product Price (xx.xx)',validators=[DataRequired()])
    productDesc = StringField('Product Description', validators=[DataRequired()])
    productCat = StringField('Product Category', validators=[DataRequired()])
    submit = SubmitField('Edit Item') 

#Edit Profile Form
class EditProfileForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    about = StringField('About', validators=[DataRequired()])
    submit = SubmitField('Submit')

#Edit User Form
class EditUserForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    about = StringField('About', validators=[DataRequired()])
    submit = SubmitField('Edit')

class EditAdminForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    submit = SubmitField('Edit')

# Register Form
class RegisterAdminForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')
# Add New Item Form
class AddItem(FlaskForm):
    productName = StringField('Product Name', validators=[DataRequired()])
    productPrice = DecimalField('Product Price (xx.xx)',validators=[DataRequired()])
    productDesc = StringField('Product Description', validators=[DataRequired()])
    productCat = StringField('Product Category', validators=[DataRequired()])
    submit = SubmitField('Add Item') 

# Edit Profile Form
class EditProfileForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    submit = SubmitField('Submit')
