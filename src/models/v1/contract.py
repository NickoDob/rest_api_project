import datetime

import pydantic


class ContractProfile(pydantic.BaseModel):
    addrApartment: str
    addrCity: str
    addrComment: str
    addrCountry: str
    addrHouse: str
    addrIndex: str
    addrName: str
    addrRegion: str
    addrStreet: str
    addrSubregion: str
    bdtId: int
    clntId: int
    cntrId: int
    contactFace: str
    contractNum: str
    dateOfBirth: datetime.datetime
    dgId: int
    dlrId: int
    etime: datetime.datetime
    gndrId: int
    inn: str
    locApartment: str
    locCity: str
    locComment: str
    locCountry: str
    locHouse: str
    locIndex: str
    locRegion: str
    locStreet: str
    locSubregion: str
    minInvoiceSum: str
    name: str
    numHistory: int
    pasport: str
    phone: str
    signDate: datetime.datetime
    stime: datetime.datetime
    trrc: str