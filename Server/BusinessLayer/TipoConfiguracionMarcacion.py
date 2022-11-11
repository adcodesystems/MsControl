import json
from DataLayer.TipoConfiguracionMarcacion_Data import *


class TipoConfiguracionMarcacion_Business:
    def Get_TipoConfiguracionMarcacionItems():
        try:
            data = TipoConfiguracionMarcacion_Data.Get_TipoConfiguracionMarcacionItems()
            jsonData = []

            for row in data:
                jsonStr = json.dumps(row.__dict__)
                jsonStr = json.loads(jsonStr)
                jsonData.append(jsonStr)

            return jsonData
        except Exception as e:
            print(e)

    def Post_TipoConfiguracionMarcacion_Insert(Ent: TipoConfiguracionMarcacionEntity):
        try:
            data = TipoConfiguracionMarcacion_Data.Post_TipoConfiguracionMarcacion_Insert(Ent)
            return data
        except Exception as e:
            print(e)


    def Post_TipoConfiguracionMarcacion_Delete(Id: int):
        try:
            data = TipoConfiguracionMarcacion_Data.Post_TipoConfiguracionMarcacion_Delete(Id)
            return data
        except Exception as e:
            print(e)

    def Update_TipoConfiguracionMarcacion_Insert(Ent: PersonaNaturalEntity):
        try:
            data = TipoConfiguracionMarcacion_Data.Update_TipoConfiguracionMarcacion_Insert(Ent)
            return data
        except Exception as e:
            print(e)
