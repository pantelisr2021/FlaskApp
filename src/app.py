from flask import Flask, render_template, redirect, url_for, request
import  urllib.request, json


app = Flask(__name__)

@app.route("/index/")
@app.route("/")
def root():
    return render_template("index.html")


@app.route("/signup/",methods=["GET","POST"])
def signup():
    print(request.form)
    return render_template("signup.html")


@app.route("/login/")
def login():
    return render_template("login.html")


@app.route("/logout/")
def logout():
    return redirect(url_for("root"))


@app.route("/new_article/")
def new_article():
    return render_template("new_article.html")

@app.route("/okairos/")
def okairos():
    return render_template("okairos.html")


if __name__ == "__main__":
    app.run(debug=True)