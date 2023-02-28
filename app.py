from flask import Flask
from .views.routes import views

app = Flask(__name__)

app.register_blueprint(views)
app.run()