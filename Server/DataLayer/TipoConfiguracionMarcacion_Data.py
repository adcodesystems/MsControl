from xmlrpc.client import Boolean
import pymysql
from sqlalchemy import true
from DataLayer.configMysql import mysql
from EntityLayer.TipoConfiguracionMarcacionEntity import *


class TipoConfiguracionMarcacion_Data:
    def Get_TipoConfiguracionMarcacionItems():
        try:
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.callproc("sp_PersonaNaturalSelectAll",)
            Rows = cursor.fetchall()

            list = []

            for row in Rows:
                Data_ent = TipoConfiguracionMarcacionEntity.Cargar(row)
                list.append(Data_ent)
            return list
        except Exception as e:
            print(e)

    def Post_TipoConfiguracionMarcacion_Insert(Ent: TipoConfiguracionMarcacionEntity):
        try:
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            args = (Ent.TIP_CON_MARID,
                    Ent.TIP_CON_MAR,
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

    def Post_TipoConfiguracionMarcacion_Delete(Id: int):
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

    def Update_TipoConfiguracionMarcacion_Insert(Ent: TipoConfiguracionMarcacionEntity):
        try:
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            args = (Ent.TIP_CON_MARID,
                    Ent.TIP_CON_MAR,
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
