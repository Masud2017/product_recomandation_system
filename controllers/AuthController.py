from flask import Blueprint,request,url_for,jsonify,flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_manager,login_required
from flask_login import current_user
from flask_login import login_user,logout_user
from ..models.Models import User,db
from flask_login import LoginManager

auth_controller = Blueprint('auth_controller',__name__)


login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(auth_controller)

@auth_controller.route("/reg",methods = ["POST","GET"])
def register_user():
    form_data = {"name":request.form["name"],"password":request.form["pass"],"user_id":request.form["uid"]}
    new_user = User(user_id=form_data["user_id"],name=form_data["name"],password=generate_password_hash(form_data["password"],method="sha256"))

    try :
        db.session.add(new_user)
        db.session.commit()
    except KeyError:
        print("Something went wrong trying to resolve it ..")
    
    return url_for("views.index")

@auth_controller.route("/generate_user_id",methods= ["GET"])
def get_new_user_id():
    pass


@auth_controller.route("/login",methods = ["POST"])
def login():
    return url_for("views.index")


@login_manager.user_loader
def load_user(user_id):
    # since the user_id is just the primary key of our user table, use it in the query for the user
    return User.query.get(int(user_id))
