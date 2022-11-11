
import json
from BusinessLayer.TipoConfiguracionMarcacion_Business import *
from app import app
from flask import request, jsonify
from function_jwt import validate_token


# @app.before_request
# def verify_token_middleware():
#     token = request.headers['Authorization'].split(" ")[1]
#     return validate_token(token,output=False)

@app.route('/Get_TipoConfiguracionMarcacionItems')
def Get_TipoConfiguracionMarcacionItems():
    try:
        jsonData = TipoConfiguracionMarcacion_Business.Get_TipoConfiguracionMarcacionItems()
        respone = jsonify(jsonData)
        respone.status_code = 200
        return respone
    except:
        print("An exception occurred")


@app.route('/Post_TipoConfiguracionMarcacion_Insert', methods=['POST'])
def Post_TipoConfiguracionMarcacion_Insert():
    try:
        if request.method == 'POST':
            m_TIP_CON_MARID = request.json['TIP_CON_MARID']
            m_TIP_CON_MAR = request.json['TIP_CON_MAR']
            m_USU_REG = request.json['USU_REG']
            m_EST_REG = request.json['EST_REG']
            Ent = TipoConfiguracionMarcacionEntity
            Ent.TIP_CON_MARID = TIP_CON_MARID
            Ent.TIP_CON_MAR = m_TIP_CON_MAR
            Ent.FEC_REG = datetime.now
            Ent.USU_REG = 'adm'
            Ent.EST_REG = True
            jsonData = TipoConfiguracionMarcacion_Business.Post_TipoConfiguracionMarcacion_Insert(Ent)

        respone = jsonify(jsonData)
        respone.status_code = 200
        return respone
    except:
        print("An exception occurred")


@app.route('/Post_TipoConfiguracionMarcacion_Delete/<Id>', methods=['DELETE'])
def Post_TipoConfiguracionMarcacion_Delete(Id):
    try:
        jsonData = TipoConfiguracionMarcacion_Business.Post_TipoConfiguracionMarcacion_Delete(
            Id)

        respone = jsonify(jsonData)
        respone.status_code = 200
        return respone
    except:
        print("An exception occurred")


@app.route('/Update_TipoConfiguracionMarcacion_Insert', methods=['POST'])
def Update_TipoConfiguracionMarcacion_Insert():
    try:
        if request.method == 'POST':
            m_TIP_CON_MARID =int( request.json['TIP_CON_MARID'])
            m_TIP_CON_MAR = request.json['TIP_CON_MAR']
            m_USU_REG = request.json['USU_REG']
            m_EST_REG = request.json['EST_REG']

            Ent = TipoConfiguracionMarcacionEntity
            Ent.TIP_CON_MARID = TIP_CON_MARID
            Ent.TIP_CON_MAR = m_TIP_CON_MAR
            Ent.FEC_REG = datetime.now
            Ent.USU_REG = 'adm'
            Ent.EST_REG = True
            jsonData = TipoConfiguracionMarcacion_Business.Update_TipoConfiguracionMarcacion_Insert(Ent)

        respone = jsonify(jsonData)
        respone.status_code = 200
        return respone
    except:
        print("An exception occurred")