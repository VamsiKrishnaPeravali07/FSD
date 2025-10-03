from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
responses = []

@app.route("/", methods=["GET", "POST"])
def survey():
    if request.method == "POST":
        name = request.form.get("name")
        favorite_movie = request.form.get("favorite_movie")
        rating = request.form.get("rating")
        genre = request.form.get("genre")
        recommend = request.form.get("recommend")
        response = {
            "name": name,
            "favorite_movie": favorite_movie,
            "rating": rating,
            "genre": genre,
            "recommend": recommend
        }
        responses.append(response)
        return redirect(url_for("thankyou"))
    return render_template("survey.html")

@app.route("/thankyou")
def thankyou():
    return render_template("responses.html", responses=responses)

if __name__ == "__main__":
    app.run(debug=True)
