from flask import Blueprint,render_template

views = Blueprint('views',__name__)

@views.route("/",methods=["GET"])
def index():
    print("Hello world index method is invoked... ")
    return render_template("home_page.html")
@views.route("/signup",methods = ["GET"])
def signup ():
    return render_template("home_page_signup.html")
