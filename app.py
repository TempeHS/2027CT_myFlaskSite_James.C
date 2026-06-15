from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/articles")
def articles():
    return render_template("articles.html")


@app.route("/article_1")
def article_1():
    return render_template("article_1.html")


@app.route("/article_2")
def article_2():
    return render_template("article_2.html")


@app.route("/article_3")
def article_3():
    return render_template("article_3.html")


@app.route("/article_4")
def article_4():
    return render_template("article_4.html")


@app.route("/Support")
def Support():
    return render_template("Support.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
