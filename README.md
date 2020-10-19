# Flask Web Application Project
Web application project done during our holidays. Done by Xerozzz, eatenlow and chloewt.

A web application template we did to learn Flask. This is a very simple skeleton that can be cloned and used for any future web application requirements that can be fulfilled by Flask, such as hackathons and other projects. Based on an E-commerce site. Deployed on AWS using EC2 and RDS (MySQL).

<b>Status:</b> Completed

### Features
- E-commerce App
- User login and registration
- Adding and deleting items from cart
- Search for items
- User profile and editing
- Category pages
- Admin login
- Admin managing of items, users and admins (Create, Delete, Edit)

### Technologies
- Python Flask
    - Flask
    - python-dotenv
    - flask-wtf
    - flask-mysql
- RDS MySQL database
- AWS EC2 Instances

## Installation
### Prerequisites
- Have python installed
- Have MySQL installed 
- Have Git installed

### Steps
1. Clone the repo using `git clone` onto your machine
2. Run `pip install -r requirements.txt` to install all your dependencies and packages
3. Run `FlaskProject.sql` in MySQL, can be Workbench or through a CLI tool, to install the database that contains mock data
4. Type `flask run` to launch the app. It will run on `http://127.0.0.1:5000/` by default