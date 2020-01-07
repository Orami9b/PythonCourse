from flask import Flask

application = Flask(__name__)

@application.route("/")
def home():
   return "Website content goes here!"

if __name__ == "__main__":
   application.run(debug = true)