from flask import Flask, url_for, render_template, request, redirect,flash,session
from stuff import phoeneticGenerator

app = Flask(__name__)
app.secret_key = "Wakatabotobilat251"

@app.route("/",methods=["POST","GET"])
def home():
    return render_template("index.html")


@app.route("/customerscript",methods=["POST","GET"])
def customerScript():
    if request.method == "POST":
       customer_info = []
       customer_info.append(request.form["generalNotes"])
       customer_info.append(request.form["fullName"])
       customer_info.append(request.form["yearMakeModel"])
       customer_info.append(request.form["issueDuration"])
       customer_info.append(request.form["anyWorkDone"])
       customer_info.append(request.form["appointment"])
       customer_info.append(request.form["customerNumber"])

       customer_info_str = ", ".join(customer_info)
       flash(customer_info_str,"info")
       return redirect(url_for("customerScript"))
    else:
        return render_template("customerscript.html")
            

@app.route("/partscript",methods=["POST","GET"])
def partScript():
    if request.method == "POST":
        if 'phoneticGenButton' in request.form:
            phoenetics = phoeneticGenerator(request.form["baseNum"])
            flash(phoenetics,"info")
        elif 'partsInfoButton' in request.form:
            parts_info = []
            parts_info.append(request.form["shopName"])
            parts_info.append(request.form["shopNumber"])
            parts_info.append(request.form["partNotes"])
            parts_info.append(request.form["partPrice"])
            parts_info.append(request.form["warranty"])
            parts_info.append(request.form["partDetails"])
            parts_info.append(request.form["quoteNumber"])
            parts_info_str = ", ".join(parts_info)
            flash(parts_info_str,"info")

        return redirect(url_for("partScript"))
    else:
        return render_template("partscript.html")

@app.route("/warrantyscript",methods=["POST","GET"])
def warrantyScript():
    if request.method == "POST":
        if 'phoneticGenButton' in request.form:
            phoenetics = phoeneticGenerator(request.form["baseNum"])
            flash(phoenetics,"info")
        elif 'warrantyInfoButton' in request.form:
            warranty_info = []
            warranty_info.append(request.form["warrantyNotes"])
            warranty_info.append(request.form["progressNotes"])
            warranty_info.append(request.form["authorizationNum"])
            warranty_info_str = ", ".join(warranty_info)
            flash(warranty_info_str,"info")
            
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