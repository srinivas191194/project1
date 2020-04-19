import os
import sys

from flask import Flask, session, render_template, request
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)


# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))


@app.route("/")
def index():
    return "<h1>Register</h1>"

@app.route("/register")
def register():
    return render_template("registration.html")

@app.route("/userDetails",methods=["POST"])
def userDetails():
    username=request.form.get("username")
    password=request.form.get("password")
    print(username,file=sys.stderr)

    return render_template("user.html" , user=username)