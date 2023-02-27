from flask import Flask,render_template

app = Flask(__name__)

@app.route("/",methods=["GET"])
def index():
    print("Hello world index method is invoked... ")
    return render_template("home_page.html")
@app.route("/signup",methods = ["GET"])
def signup ():
    return render_template("home_page_signup.html")

if __name__ == "__main__":
    print("Starting the server")
    app.run()