from flask import Blueprint,render_template
from pymongo import MongoClient

views = Blueprint('views',__name__)

@views.route("/",methods=["GET"])
def index():
    client = MongoClient("localhost",27017)
    recomandation_system_db = client.recomandation_system
    restaurants_visited_collection = recomandation_system_db.restaurants_visited
    cuisine_collection = recomandation_system_db.cusine_and_type
    table_data = restaurants_visited_collection.find()
    cusine_table_data = cuisine_collection.find()


    return render_template("home_page.html")
@views.route("/signup",methods = ["GET"])
def signup ():
    return render_template("home_page_signup.html")
