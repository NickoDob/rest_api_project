import datetime
from fastapi import APIRouter
from fastapi import Query
from config import Settings
from models.v1.subs import SetSubsOptData
from services.v1.methods import ClientMethods

methods = ClientMethods()
config = Settings()

# Экземпляр класса APIRouter для создания операций пути
router = APIRouter(
    prefix='/subs',
    tags=["Subscriber"],
)

# Параметры для подключения методов к InvApiCore
parameters = {
        'outContractName': config.outContractName,
        'userLogin': config.userLogin,
        'targetDate': datetime.datetime.now().isoformat(),
        }


# Метод получения информации о профиле абонента
@router.get("/subs-profile")
async def get_subs_profile(msisdn: int = Query(None, description="Номер телефона"),
                           subsId: int = Query(None, description="Идентификатор абонента"),
                           inContractSign: str = Query(examples={
                               "by_msisdn": {"summary": "По номеру телефона", "value": "by_msisdn"},
                               "by_subscriber_id": {"summary": "По идентификатору абонента", "value": "by_subscriber_id"}
                           }, description='Входные контракты'),
                           ):
    params = parameters.copy()
    params['msisdn'] = msisdn
    params['subsId'] = subsId
    params['inContractSign'] = inContractSign
    result = methods.get_subs_profile(params)
    methods.log_history(request="GetSubsProfile", datetime=params['targetDate'])
    return result


# Метод получения дополнительных сведений профиля абонента
@router.get("/get_subs_opt")
async def get_subs_opt_data(subsId: int = Query(None, description="Идентификатор абонента"),
                            subsFldId: int = Query(None, description="Идентификатор дополнительного поля абонента"),
                            inContractSign: str = Query(examples={
                                "by_subs_id": {"summary": "По идентификатору абонента", "value": "by_subs_id"},
                                "by_in_fld_id": {"summary": "По идентификатору дополнительного поля абонента",
                                                 "value": "by_in_fld_id"},
                                "by_out_fld_id": {"summary": "По идентификатору дополнительного поля абонента",
                                                  "value": "by_out_fld_id"},
                            }, description="Входные контракты")):
    params = parameters.copy()
    params['subsId'] = subsId
    params['subsFldId'] = subsFldId
    params['inContractSign'] = inContractSign
    result = methods.get_subs_opt_data(params)
    methods.log_history(request="GetSubsOptData", datetime=params['targetDate'])
    return result


# Метод изменения дополнительных сведений профиля абонента
@router.put("/set_subs_opt")
async def set_subs_opt_data(setSubsOptData: SetSubsOptData):
    params = parameters.copy()
    params['inContractSign'] = 'by_opt_data'
    params['subsOptData'] = {
        'subsId': setSubsOptData.subsId,
        'subsFldId': setSubsOptData.subsFldId,
        'fieldValue': setSubsOptData.subsFieldValue
    }
    result = methods.set_subs_opt_data(params)
    methods.log_history(request="SetSubsOptData", datetime=params['targetDate'])
    return result