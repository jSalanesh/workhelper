from flask import Flask, url_for, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/dailytask")
def dailyTask():
    return render_template("dailytask.html")

@app.route("/roreview")
def repairOrderReview():
    return render_template("roreview.html")

if __name__ == "main":
    app.run()