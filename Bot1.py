from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    return "Bot 1 is running!"

if __name__ == "__main__":
    app.run()