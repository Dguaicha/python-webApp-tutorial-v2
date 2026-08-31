from flask import Flask, jsonify, render_template

app = Flask(__name__)

JOBS = [
    {"id": 1, "title": "data analyst", "location": "India", "salary": "2k usd"},
    {"id": 2, "title": "data scientist", "location": "India", "salary": "2k usd"},
    {"id": 3, "title": "frontend developer", "location": "India", "salary": "2k usd"},
    {"id": 4, "title": "fullstack developer", "location": "India", "salary": "2k usd"},
]


@app.route("/")
def hello_world():
    return render_template("home.html", jobs=JOBS)


@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
