from flask import Flask
from .views.routes import views
from .controllers.AuthController import auth_controller
from flask_migrate import Migrate


from .models.Models import db


app = Flask(__name__)

app.config['SECRET_KEY'] = '''
17d5aa40c37d76a7f30feb6af4aae9823c5d658e13c808d1edbb83d980257654
d06dafca1740a0585f0e4a43d9e8ff459d8be39d811ac2982a24fbd195c68aaf
31bf0092872bf7ada95a4e301bfe3fe59d8e440bdbf37cb4ff7dcba110a49c56
8b14a72cbfc556c9ca28eddc389f976817f8060ca17fe00a42ddcaaeab18bd11
ca4da398de53c194b8be98b659a3779e37f7cef58e48f653ef33f0d3c2f7a84d
a3ea77d0af9b94c9955086012b35c50d9e5fcb40536c990449319047c9950150
d92259b22730a1623c85aae43f532d2025ecfd8daef23c694fe8005db0b4630b
f240f33a2c5d93839b08fefb16ed7bfb4fb9295dbd6c59c5712851e4dd6e1c4f
0c1069edf0d5c3a17150f34dab7ea90900692430a39fc7ef9fe68ac7e3c04f2f
4907a450c5eb01eb334ae030912077d091f0f710acf00ed342f519807954a36b
'''
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"

db.init_app(app)
migrate = Migrate(app, db,render_as_batch=True)

with app.app_context():
    db.create_all()

app.register_blueprint(views)
app.register_blueprint(auth_controller)



# Load one time after the first startup
from .models.Models import User
from pymongo import MongoClient
from werkzeug.security import generate_password_hash


@app.before_first_request
def seed_mongo_users_to_db():
    client = MongoClient("localhost",27017)
    recomandation_system_db = client.recomandation_system
    restaurants_visited_collection = recomandation_system_db.restaurants_visited

    table_data = restaurants_visited_collection.find()

    for x in table_data:
        exists = db.session.query(db.exists().where(User.user_id == x["userID"])).scalar()
        if not exists:
            temp_user = User(name = "Existing_user_"+x["userID"],user_id=x["userID"],password=generate_password_hash("12345678","sha256"))
            db.session.add(temp_user)
            db.session.commit()
        else:
            continue

if __name__ == "__main__":
    app.run()