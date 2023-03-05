from flask import Flask,Blueprint

auth_controller = Blueprint('auth_controller',__name__)

@auth_controller.route("/reg",methods = ["POST"])
def register_user():
    pass