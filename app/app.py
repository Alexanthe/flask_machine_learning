# set FLASK_APP = app.py
# $env:FLASK_ENV = "development"  # ON debug mode
# flask run

# pip freeze > requirements.txt

from flask import Flask, render_template, request, redirect

import sys

sys.path.append(r"C:\Users\alexa\Documents\GitHub\flask_machine_learning\app\model")
# sys.path.append(".\model")
from model import models

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
        sim_msg = models.over_model(data_list)
        result["sim_msg"] = sim_msg
        return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(port=8080, host="0.0.0.0")
