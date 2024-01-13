#!/bin/python3
from flask import Flask, request, jsonify, Response

products = [{"iphone": 10000, 
            "samsung": 8000, 
            "xiaomi": 5000}]

students = [{"name": "Kumar", 
            "class": 12, 
            "grade": "A"} ]

app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello World!'

# @app.route('/api', methods=["GET", "POST"])
# def api():
#     if request.method == 'GET':
#         return ("You are getting a get request")
#     elif request.method == 'POST':
#         return ("You are getting a post request")
#     else:
#         return ("You are getting a wrong request")

# @app.route('/product', methods=["GET", "POST"])
# def product():
#     if request.method == 'GET':
#         return jsonify(products)
#     elif request.method == 'POST':
#         jsondata = request.get_json(force=True)
#         products.append(jsondata)
#         return ("You are getting a post request")
#     else:
#         return ("You are getting a wrong request")
    
@app.route('/student', methods=["GET", "POST"])
def student():
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