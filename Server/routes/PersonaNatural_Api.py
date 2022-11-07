
import json
from BusinessLayer.PersonaNatural_Business import *
from app import app
from flask import request, jsonify
from function_jwt import validate_token


# @app.before_request
# def verify_token_middleware():
#     token = request.headers['Authorization'].split(" ")[1]
#     return validate_token(token,output=False)

@app.route('/Get_PersonaNaturalItems')
def Get_PersonaNaturalItems():
    try:
        jsonData = PersonaNatural_Business.Get_PersonaNaturalItems()
        respone = jsonify(jsonData)
        respone.status_code = 200
        return respone
    except:
        print("An exception occurred")


@app.route('/Post_PersonaNatural_Insert', methods=['POST'])
def Post_PersonaNatural_Insertaa():
    try:
        if request.method == 'POST':
            m_PERID = request.json['PERID']
            m_DOC_PER = request.json['DOC_PER']
            m_NOM_PER = request.json['NOM_PER']
            m_APE_PAT = request.json['APE_PAT']
            m_APE_MAT = request.json['APE_MAT']

            Ent = PersonaNaturalEntity
            Ent.PERID = m_PERID
            Ent.TIP_DOCID = 1
            Ent.DOC_PER = m_DOC_PER
            Ent.NOM_PER = m_NOM_PER
            Ent.APE_PAT = m_APE_PAT
            Ent.APE_MAT = m_APE_MAT
            Ent.FEC_NAC = datetime.now
            Ent.FEC_VEC = datetime.now
            Ent.TIP_SEXID = 1
            Ent.TIP_CIVID = 1
            Ent.DIR = 'FG'
            Ent.DIR_REF = 'DRE'
            Ent.UBIID = 0
            Ent.FEC_REG = datetime.now
            Ent.USU_REG = 'adm'
            Ent.EST_REG = True
            jsonData = PersonaNatural_Business.Post_PersonaNatural_Insert(Ent)

        respone = jsonify(jsonData)
        respone.status_code = 200
        return respone
    except:
        print("An exception occurred")


@app.route('/PersonaNatural_Delete/<Id>', methods=['DELETE'])
def Post_PersonaNatural_Deletee(Id):
    try:
        jsonData = PersonaNatural_Business.Post_PersonaNatural_Delete(
            Id)

        respone = jsonify(jsonData)
        respone.status_code = 200
        return respone
    except:
        print("An exception occurred")


@app.route('/update_PersonaNatural_Insert', methods=['POST'])
def Update_PersonaNatural_Insert():
    try:
        if request.method == 'POST':
            m_PERID =int( request.json['PERID'])
            m_DOC_PER = request.json['DOC_PER']
            m_NOM_PER = request.json['NOM_PER']
            m_APE_PAT = request.json['APE_PAT']
            m_APE_MAT = request.json['APE_MAT']

            Ent = PersonaNaturalEntity
            Ent.PERID = m_PERID
            Ent.TIP_DOCID = 1
            Ent.DOC_PER = m_DOC_PER
            Ent.NOM_PER = m_NOM_PER
            Ent.APE_PAT = m_APE_PAT
            Ent.APE_MAT = m_APE_MAT
            Ent.FEC_NAC = datetime.now
            Ent.FEC_VEC = datetime.now
            Ent.TIP_SEXID = 1
            Ent.TIP_CIVID = 1
            Ent.DIR = 'FG'
            Ent.DIR_REF = 'DRE'
            Ent.UBIID = 0
            Ent.FEC_REG = datetime.now
            Ent.USU_REG = 'adm'
            Ent.EST_REG = True
            jsonData = PersonaNatural_Business.Update_PersonaNatural_Insert(Ent)

        respone = jsonify(jsonData)
        respone.status_code = 200
        return respone
    except:
        print("An exception occurred")