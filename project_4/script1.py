from flask import Flask

application = Flask(__name__)

@application.route("/")
def home():
   return "Here is the home page!"

@application.route("/about/")
def about():
   return "About content goes here!"

if __name__ == "__main__":
   application.run(debug = True)