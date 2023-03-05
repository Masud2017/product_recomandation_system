from flask import Flask
from .views.routes import views
from .controllers.AuthController import auth_controller

app = Flask(__name__)

if __name__ == "__main__":
    app.register_blueprint(views)
    app.register_blueprint(auth_controller)
    app.run()