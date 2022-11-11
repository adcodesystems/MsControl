from datetime import datetime


class TipoConfiguracionMarcacionEntity:
    TIP_CON_MARID: int
    TIP_CON_MAR: str
    FEC_REG: datetime
    USU_REG: str
    EST_REG: bool

    def Cargar(_json: any):
        c = TipoConfiguracionMarcacionEntity()
        c.TIP_CON_MARID = _json['TIP_CON_MARID']
        c.TIP_CON_MAR = _json['TIP_CON_MAR']
        c.USU_REG = _json['USU_REG']
        c.EST_REG = bool(_json['EST_REG'])
        return c