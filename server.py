import numpy as np
from flask import Flask, render_template, request
from function import *
app = Flask(__name__)
@app.route("/")
def index():
    return render_template("main.html")

@app.route("/", methods = ["POST"])
def result():
    answer = np.array([request.form['q1'], request.form['q2'], request.form['q3'], request.form['q4'], request.form['q5'], request.form['q6'], request.form['q7'], request.form['q8'], request.form['q9'], request.form['q10']]).astype(np.int64)
    hobby = {}
    hobby["스포츠"] = fav(np.array([0, 0, 1, 0, 1, 1, 1, 1, 1, 0]))
    hobby["소비"] = fav(np.array([0, -1, 0, 0, 0, 0, -1, 0, 0, 0]))
    hobby["19금"] = fav(np.array([-1, -1, -1, 0, 0, 0, -1, 0, 0, 0]))
    hobby["수집"] = fav(np.array([0, -1, 0, -1, 0, 0, -1, 0, 0, 0]))
    hobby["게임"] = fav(np.array([0, 0, 0, 1, 0, 1, -1, 0, 0, 1]))
    hobby["무술"] = fav(np.array([0, 0, 1, 0, 1, 1, 1, 1, 0, 0]))
    hobby["창작적"] = fav(np.array([0, 0, 1, 1, 0, -1, -1, 1, 0, 0]))
    li = []
    for key in hobby.keys():
        hob = hobby[key]
        hob.score(np.sum(np.multiply(hob.pre, answer)))
        li.append([key, hob.sco])

    return render_template("result.html", ranking = li)

port_num = 8080

if __name__ == "__main__":
    app.run(port = port_num)