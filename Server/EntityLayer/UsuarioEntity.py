from datetime import datetime

class UsuarioEntity:
    USU_ID : int
    PERID: int
    COD_ID: str
    PWD :str
    FEC_VIG: datetime
    FEC_REG: datetime
    USU_REG: str
    EST_REG: bool

    def Cargar(_DB: any):
        c = UsuarioEntity()
        c.USU_ID = _DB['USU_ID']
        c.PERID = _DB['PERID']
        c.COD_ID = _DB['COD_ID']
        c.PWD = _DB['PWD']
        c.FEC_VIG = _DB['FEC_VIG']
        c.FEC_REG = _DB['FEC_REG']
        c.USU_REG = _DB['USU_REG']
        c.EST_REG = bool(_DB['EST_REG'])
        return c

    def CargarAcceso(_DB: any):
        c = UsuarioEntity()
        c.PERID = _DB['PERID']
        c.FEC_VIG = _DB['FEC_VIG']
        c.USU_REG = _DB['USU_REG']
        c.EST_REG = bool(_DB['EST_REG'])
        return c