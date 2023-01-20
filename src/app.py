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


@app.route("/movies/")
def get_movies_list():
    url = "https://api.themoviedb.org/3/movie/popular?api_key=18a017b1725a276ac9a9838ec5345147"

    response = urllib.request.urlopen(url)
    data = response.read()
    jsondata = json.loads(data)

    movie_json = []
    
    for movie in jsondata["results"]:
        movie = {
            "title": movie["title"],
            "overview": movie["overview"],
        }
        
        movie_json.append(movie)
    print(movie_json)
    return {"movie title": movie_json}


if __name__ == "__main__":
    app.run(debug=True)