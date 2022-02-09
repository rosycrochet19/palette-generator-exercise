from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.static_folder = "static"
Bootstrap(app)
db = SQLAlchemy(app)

from application import routes