from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def index():
    return "Congratulations, it's a web app!"

print("Hello World")

roles = ["Liberal", "Fascist"]

print("Your role is: " + random.choice(roles))
