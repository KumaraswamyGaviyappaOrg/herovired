#!/bin/python3
from flask import Flask, request, jsonify

#creatring a flask app
students = [{"name": "Kumar", 
            "class": 12, 
            "grade": "A"} ]

app = Flask(__name__)


@app.route('/students', methods=["GET", "POST"])
def students():
    if request.method == 'GET':
        return jsonify(students)
    elif request.method == 'POST':
        jsondata = request.get_json(force=True)
        students.append(jsondata)
        return ("You are getting a post request")
    else:
        return ("You are getting a wrong request")

#app.run(host='0.0.0.0', port=80)

if __name__ == '__main__':
    app.run(debug=True)


#this for testing purpose