# models2/model.py
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func, CheckConstrait

app = Flask(__name__)
app.config[]
app.config[] = False
app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy(app)


