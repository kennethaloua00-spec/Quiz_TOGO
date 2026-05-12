from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot WhatsApp actif 🚀"

app.run()