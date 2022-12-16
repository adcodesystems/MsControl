
import json
from BusinessLayer.Usuario_Business import *
from app import app
from flask import request, jsonify
from function_jwt import validate_token


# @app.before_request
# def verify_token_middleware():
#     token = request.headers['Authorization'].split(" ")[1]
#     return validate_token(token,output=False)

@app.route('/Usuario/GetAcceso/<usu>/<pwd>')
def Get_Acceso(usu: str, pwd: str):
    try:
        jsonData = Usuario_Business.Get_Acceso(usu,pwd)
        respone = jsonify(jsonData)
        respone.status_code = 200
        return respone
    except:
        print("An exception occurred")
