from datetime import datetime


class PersonaNaturalEntity:
    PERID: int
    TIP_DOCID: int
    DOC_PER: str
    NOM_PER: str
    APE_PAT: str
    APE_MAT: str
    FEC_NAC: datetime
    FEC_VEC: datetime
    TIP_SEXID: int
    TIP_CIVID: int
    DIR: str
    DIR_REF: str
    UBIID: int
    FEC_REG: datetime
    USU_REG: str
    EST_REG: bool

    def Cargar(_json: any):
        c = PersonaNaturalEntity()
        c.PERID = _json['PERID']
        c.TIP_DOCID = _json['TIP_DOCID']
        c.DOC_PER = _json['DOC_PER']
        c.NOM_PER = _json['NOM_PER']
        c.APE_PAT = _json['APE_PAT']
        c.APE_MAT = _json['APE_MAT']
        # c.FEC_NAC = datetime(_json['FEC_NAC'])
        # c.FEC_VEC = datetime(_json['FEC_VEC'])
        c.TIP_SEXID = _json['TIP_SEXID']
        c.TIP_CIVID = _json['TIP_CIVID']
        c.DIR = _json['DIR']
        c.DIR_REF = _json['DIR_REF']
        c.UBIID = _json['UBIID']
        # c.FEC_REG = datetime(_json['FEC_REG'])
        c.USU_REG = _json['USU_REG']
        c.EST_REG = bool(_json['EST_REG'])
        return c

    def CargarSoloNombre(_json: any):
        c = PersonaNaturalEntity()
        c.PERID = _json['PERID']
        c.DOC_PER = _json['DOC_PER']
        c.NOM_PER = _json['NOM_PER']
        c.APE_PAT = _json['APE_PAT']
        c.APE_MAT = _json['APE_MAT']
        return c
