from xmlrpc.client import Boolean
import pymysql
from sqlalchemy import true
from DataLayer.configMysql import mysql
from EntityLayer.PersonaNaturalEntity import *


class PersonaNatural_Data:
    def Get_PersonaNaturalItems():
        try:
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.callproc("sp_PersonaNaturalSelectAll")
            Rows = cursor.fetchall()

            list = []

            for row in Rows:
                print(row)
                Data_ent = PersonaNaturalEntity.CargarSoloNombre(row)
                list.append(Data_ent)
            print(list)
            return list
        except Exception as e:
            print(e)

    