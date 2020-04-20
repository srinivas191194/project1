from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
class user(db.Model):

    __tablename__ = "Table"

    username = db.Column(db.String, unique = True, nullable = False, primary_key = True)
    password = db.Column(db.String, nullable = False)
    time = db.Column(db.DateTime, nullable = False)
