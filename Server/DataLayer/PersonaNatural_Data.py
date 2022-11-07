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
            cursor.callproc("sp_PersonaNaturalSelectAll",)
            Rows = cursor.fetchall()

            list = []

            for row in Rows:
                Data_ent = PersonaNaturalEntity.CargarSoloNombre(row)
                list.append(Data_ent)
            return list
        except Exception as e:
            print(e)

    def Post_PersonaNatural_Insert(Ent: PersonaNaturalEntity):
        try:
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            args = (Ent.TIP_DOCID,
                    Ent.DOC_PER,
                    Ent.NOM_PER,
                    Ent.APE_PAT,
                    Ent.APE_MAT,
                    Ent.FEC_NAC,
                    Ent.FEC_VEC,
                    Ent.TIP_SEXID,
                    Ent.TIP_CIVID,
                    Ent.DIR,
                    Ent.DIR_REF,
                    Ent.UBIID,
                    Ent.FEC_REG,
                    Ent.USU_REG,
                    Ent.EST_REG) 

            result_args = cursor.callproc("sp_PersonaNaturalInsert", args)

            conn.commit()
            # print(result_args[0])
            return True
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()

    def Post_PersonaNatural_Delete(Id: int):
        try:
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            args = (Id,) 
            result_args = cursor.callproc("sp_PersonaNaturalDelete", args)
            conn.commit()
            return True
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()

    def Update_PersonaNatural_Insert(Ent: PersonaNaturalEntity):
        try:
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            args = (Ent.PERID,
                    Ent.TIP_DOCID,
                    Ent.DOC_PER,
                    Ent.NOM_PER,
                    Ent.APE_PAT,
                    Ent.APE_MAT,
                    Ent.FEC_NAC,
                    Ent.FEC_VEC,
                    Ent.TIP_SEXID,
                    Ent.TIP_CIVID,
                    Ent.DIR,
                    Ent.DIR_REF,
                    Ent.UBIID,
                    Ent.FEC_REG,
                    Ent.USU_REG,
                    Ent.EST_REG) 

            result_args = cursor.callproc("sp_PersonaNaturalUpdate", args)

            conn.commit()
            # print(result_args[0])
            return True
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()
