# set FLASK_APP = app.py
# $env:FLASK_ENV = "development"  # ON debug mode
# flask run

# pip freeze > requirements.txt

from flask import Flask, render_template, request, redirect

import sys
import random
import string

# import mysql.connector

import model.models as models

# import preprocess

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

        #     mydb = mysql.connector.connect(
        #     host="edc3a984-eedd-4396-851b-823320a16114.mysql.service.internal",
        #     user="87188e870a444fa7b278aa0622f327ce",
        #     password="qvf8x0ttgzvvhqzj",
        #     db="service_instance_db",
        # )
        #     # get len of database and declare in insert
        #     mycursor = mydb.cursor(dictionary=True)
        #     mycursor.execute('SELECT count(id) FROM current_cases')
        #     lenDb = mycursor.fetchone()
        #     lenDb = str(lenDb)

        #     # do list of name, age, ic
        #     name = ["Alex","James","Ashley","Debbie"]
        #     name = random.choice(name)

        #     age = str(random.randint(21,65))

        #     ic ='S'+age+''.join([random.choice(string.digits
        #         + string.digits) for n in range(5)]) + ''.join([random.choice(string.ascii_letters
        #         + string.digits) for n in range(1)]).upper()

        # fix location, and further prediction and other things
        # put sentence_1 and sim_msg in symptoms and tag123 respectively
        # connection
        return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(port=8080, host="0.0.0.0")
