from xmlrpc.client import Boolean
import pymysql
from sqlalchemy import true
from DataLayer.configMysql import mysql
from EntityLayer.UsuarioEntity import *


class Usuario_Data:
    def Get_Acceso(v_COD_ID: str, v_PWD: str):
        try:
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.callproc("sp_AccsoUsuario", args=(v_COD_ID, v_PWD))
            Rows = cursor.fetchall()

            list = []

            for row in Rows:
                Data_ent = UsuarioEntity.CargarAcceso(row)
                list.append(Data_ent)
            return list
        except Exception as e:
            print(e)
