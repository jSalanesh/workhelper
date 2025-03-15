from flask import Flask, url_for, render_template, request, redirect,flash,session

app = Flask(__name__)
app.secret_key = "Wakatabotobilat251"

@app.route("/",methods=["POST","GET"])
def home():
    return render_template("index.html")


@app.route("/customerscript",methods=["POST","GET"])
def customerScript():
    return render_template("customerscript.html")

@app.route("/partscript",methods=["POST","GET"])
def partScript():
    if request.method == "POST":
        base_num = request.form["baseNum"]
        flash(base_num,"info")
        return redirect(url_for("partScript"))
    else:
        return render_template("partscript.html")

@app.route("/warrantyscript",methods=["POST","GET"])
def warrantyScript():
    if request.method == "POST":
        base_num = request.form["baseNum"]
        flash(base_num,"info")
        return redirect(url_for("warrantyScript"))
    else:
        return render_template("warrantyscript.html")

@app.route("/dailytask")
def dailyTask():
    return render_template("dailytask.html")

@app.route("/actionitems")
def actionItems():
    return render_template("actionitems.html")

@app.route("/roreview")
def repairOrderReview():
    return render_template("roreview.html")

if __name__ == "main":
    app.run()