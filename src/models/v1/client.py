import datetime
from decimal import Decimal

import pydantic


class Client(pydantic.BaseModel):
    account: Decimal
    branchId: Decimal
    clntId: Decimal
    ctId: Decimal
    currId: Decimal
    customerId: Decimal
    firstInvoiceDate: datetime.datetime
    ownerClntId: int
    parentClntId: Decimal
    prId: int
    taxRate: Decimal


class ClientHistory(pydantic.BaseModel):
    accountDeptMax: int
    balLevelControlType: str
    billingSign: int
    branchId: int
    cjtId: int
    clntId: int
    cptId: int
    credCatControlType: str
    cscId: int
    email: str
    etime: datetime.datetime
    fax: str
    finBlockSetType: str
    langId: int
    managerUserId: int
    numHistory: int
    ownerClntId: int
    statId: int
    stime: datetime.datetime
    trplId: int
    useCascadeBalance: int


class ClientOptData(pydantic.BaseModel):
    clntFldId: int
    etime: datetime.datetime
    fieldName: str
    fieldValue: str
    numHistory: int
    stime: str
    uftId: int


class SetClientOptData(pydantic.BaseModel):
    clntId: int
    clntFldId: int
    clntFieldValue: int
    inContractSign: str = 'by_opt_data'