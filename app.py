from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def introduction():
    return render_template("introduction.html")


@app.route("/skills")
def skills():
    return render_template("skills.html")

@app.route("/contactus")
def contactus():
    return render_template("contactus.html")

@app.route("/terms")
def terms():
    return render_template("terms.html")

@app.route("/privacy")
def privacy():
    return render_template("privacy.html")


app.run(debug=True)

