import datetime
from typing import List
from .client import ClientHistory, Client

import pydantic


class SubsHistory(pydantic.BaseModel):
    clntId: int
    closeDate: datetime.datetime
    cscId: int
    etime: datetime.datetime
    numHistory: int
    phoneId: int
    rlbId: int
    stId: int
    statId: int
    stime: datetime.datetime
    subsId: int
    trplId: int
    utpStatId: int
    weight: int
    zoneId: int


class Phone(pydantic.BaseModel):
    msisdn: int
    phoneId: int


class Subscriber(pydantic.BaseModel):
    activationDate: datetime.datetime
    avgCharge: str
    contact: int
    firstCall: datetime.datetime
    lastCall: datetime.datetime
    registrationDate: datetime.datetime
    subsId: int


class SubsProfile(pydantic.BaseModel):
    client: List[Client]
    clientHistory: List[ClientHistory]
    phone: List[Phone]
    subsHistory: List[SubsHistory]
    subscriber: List[Subscriber]
    broadbandParm: List
    ipAddress: List
    part: List
    subsComment: List
    subsInfo: List
    subsOptData: List


class SubsOptData(pydantic.BaseModel):
    etime: datetime.datetime
    fieldName: str
    fieldValue: str
    numHistory: int
    stime: datetime.datetime
    subsFldId: int
    subsId: int
    uftId: int


class SetSubsOptData(pydantic.BaseModel):
    subsId: int
    subsFldId: int
    subsFieldValue: int
    inContractSign: str = 'by_opt_data'
