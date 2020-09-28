from flask import Flask
from config import Config
from flaskext.mysql import MySQL

app = Flask(__name__)
app.config.from_object(Config)

MySQL = MySQL()
MySQL.init_app(app)

app.config['MYSQL_DATABASE_HOST'] = 'project-database.cokyaqjxq7d8.ap-southeast-1.rds.amazonaws.com'
app.config['MYSQL_DATABASE_PORT'] = 3306
app.config['MYSQL_DATABASE_USER'] = "admin"
app.config['MYSQL_DATABASE_PASSWORD'] = 'chloeisgay'
app.config['MYSQL_DATABASE_DB'] = 'flask'

conn = MySQL.connect()

from app import routes