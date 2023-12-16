from flask import Blueprint, render_template

Homepage = Blueprint(__name__, "Homepage")

@Homepage.route("/")
def home():
    return render_template("index.html")