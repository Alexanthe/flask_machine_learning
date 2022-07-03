# set FLASK_APP = app.py
# $env:FLASK_ENV = "development"  # ON debug mode
# flask run

from flask import Flask, render_template, request, redirect

import sys

sys.path.append(".\model")
import model

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "GET":
        return render_template("index.html")

    if request.method == "POST":
        result = request.form.to_dict(flat=True)
        sentence_1 = result.get("sentence-1")
        data_list = []
        data_list.append(sentence_1)
        sim_msg = model.over_model(data_list)
        result["sim_msg"] = sim_msg
        return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)


# from flask import Flask, render_template, request, render_template_string

# app = Flask(__name__)


# @app.route("/")
# def index():
#     return render_template("index.html")


# if __name__ == "__main__":
#     app.run(debug=True)


# @app.route("/home")
# def home_page():
#     return render_template("home.html")


# @app.route("/about")
# def about():
#     return "About this project.."
