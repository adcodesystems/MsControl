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

    def Cargar(_DB: any):
        c = PersonaNaturalEntity()
        c.PERID = _DB['PERID']
        c.TIP_DOCID = _DB['TIP_DOCID']
        c.DOC_PER = _DB['DOC_PER']
        c.NOM_PER = _DB['NOM_PER']
        c.APE_PAT = _DB['APE_PAT']
        c.APE_MAT = _DB['APE_MAT']
        # c.FEC_NAC = datetime(_json['FEC_NAC'])
        # c.FEC_VEC = datetime(_json['FEC_VEC'])
        c.TIP_SEXID = _DB['TIP_SEXID']
        c.TIP_CIVID = _DB['TIP_CIVID']
        c.DIR = _DB['DIR']
        c.DIR_REF = _DB['DIR_REF']
        c.UBIID = _DB['UBIID']
        # c.FEC_REG = datetime(_json['FEC_REG'])
        c.USU_REG = _DB['USU_REG']
        c.EST_REG = bool(_DB['EST_REG'])
        return c

    def CargarSoloNombre(_DB: any):
        c = PersonaNaturalEntity()
        c.PERID = _DB['PERID']
        c.DOC_PER = _DB['DOC_PER']
        c.NOM_PER = _DB['NOM_PER']
        c.APE_PAT = _DB['APE_PAT']
        c.APE_MAT = _DB['APE_MAT']
        return c

    def CargarSoloNombreId(_DB: any):
        c = PersonaNaturalEntity()
        c.PERID = _DB['PERID']
        return c