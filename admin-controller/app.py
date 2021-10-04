import time
import os
from flask import Flask, jsonify,request
import json
from os import path, write
from typing import ClassVar
from flask import Blueprint, render_template, request
from flask.wrappers import Response
from flask import request
from flask import jsonify
from werkzeug.wrappers.request import PlainRequest


def a_help(result):
    a_file = open("data/number.txt", "w")
    a_file.write(str(result))
    a_file.close()

def b_help(result):
    file = open("data/day.txt","w")
    file.write(str(result))
    file.close()

def data_delete(result):
    file = open("data/data.json","w")
    file.write(str(result))
    file.close()




app = Flask(__name__)


@app.route("/pcdata")
def pcname():
    pchostname = request.args.get("hostname")
    pcip = request.args.get("ip")
    pcuseranme = request.args.get("username")
    # data = {s
    #     "pc-name":f"{pcname}"
    # }

    with open("data/number.txt","r+") as file:
        number = file.read()
        next_steps = int(number) +1
        a_help(next_steps)

    with open("data/day.txt","r+") as file:
        day_data = file.read()
        rtime = time.localtime()
        day = rtime.tm_mday
        data_replay = "[]"
        day_data_convert = int(day_data)
        print(day_data)
        print(day)
        if day_data_convert == day:
            pass
        else:
            b_help(day)
            data_delete(data_replay)



    data = []
    with open("data/data.json") as file:
        data = json.load(file)
        
    data.append({"pc-hostname":pchostname,"pc-username":pcuseranme,"pc-ip":pcip,"user_add_number":next_steps})
    with open("data/data.json", "w") as file:
        json.dump(data, file)





    # f = open("data/number.txt","w")
    # number = f.read()
    # next_number = int(number)+1
    # print(next_number)
    # f.write(f"{next_number}")

    return jsonify(f"OK"),302


@app.route("/")
def index():
    return render_template("index.html"),200;  





# @app.route("/pcip")
# def pcip():
#     pcip = request.args.get("ip")

#     # data = []

#     # with open("data/ip.json") as file:
#     #     data = json.load(file)
        
#     # data.append({"pc-ip":pcip})
    
#     # with open("data/ip.json", "w") as file:
#     #     json.dump(data, file)

#     with open("data/data.json","r+") as file:
#         data = json.load(file)
#         data["pc-ip"] = pcip

#         file.seek(1)
#         json.dump(data, file)
#         file.truncate()

    

    # return jsonify("oK"),302







if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)