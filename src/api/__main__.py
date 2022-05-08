# Author  : Snehashish Laskar
# Date of creation : 08-05-2022

from flask import Flask, request, jsonify, abort
from db import *

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST', 'DEL'])

def main():

    if request.method == 'GET':
        if "taskname" in request.args:
            return jsonify(Return(request.args["taskname"]))


        elif request.args == {}:
            return jsonify(Return())

        elif "completed" in request.args:

            return jsonify(returnCompleted())

    if request.method == "POST":

        if "taskname" in request.args and "tag" in request.args and "deadline" in request.args and "importance" in request.args:
            name = request.args["taskname"]
            tag = request.args["tag"]
            deadline = request.args["deadline"]
            importance = request.args["importance"]

            createTask(name, tag, deadline, importance)
            return jsonify(Return())


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port = 1690)


