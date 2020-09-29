from flask import Flask
from config import Config
from flaskext.mysql import MySQL
import os

app = Flask(__name__)
app.config.from_object(Config)

MySQL = MySQL()
MySQL.init_app(app)

# Database config
app.config['MYSQL_DATABASE_HOST'] = os.getenv('MYSQL_DATABASE_HOST')
app.config['MYSQL_DATABASE_PORT'] = int(os.getenv('MYSQL_DATABASE_PORT'))
app.config['MYSQL_DATABASE_USER'] = os.getenv('MYSQL_DATABASE_USER')
app.config['MYSQL_DATABASE_PASSWORD'] = os.getenv('MYSQL_DATABASE_PASSWORD')
app.config['MYSQL_DATABASE_DB'] = os.getenv('MYSQL_DATABASE_DB')

conn = MySQL.connect()

from app import routes