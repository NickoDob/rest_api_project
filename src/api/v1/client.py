import datetime
from fastapi import APIRouter
from fastapi import Query
from config import Settings
from models.v1.client import SetClientOptData
from services.v1.methods import ClientMethods


methods = ClientMethods()
config = Settings()

# Экземпляр класса APIRouter для создания операций пути
router = APIRouter(
    prefix='/client',
    tags=["Client"],
)

# Параметры для подключения методов к InvApiCore
parameters = {
        'outContractName': config.outContractName,
        'userLogin': config.userLogin,
        'targetDate': datetime.datetime.now().isoformat(),
        }


# Метод получения информации о профиле клиента
@router.get("/client-profile")
async def get_client_profile(clntId: int = Query(None, description="Идентификатор клиента"),
                             account: int = Query(None, description="Лицевой счет"),
                             parentClntId: int = Query(None, description="Идентификатор головного клиента"),
                             subsStatId: int = Query(None, description="Идентификатор статуса абонента"),
                             customerId: int = Query(None, description="Идентификатор регистрационных данных"),
                             inContractSign: str = Query(examples={
                                 "by_clnt_id": {"summary": "По идентификатору клиента", "value": "by_clnt_id"},
                                 "by_account": {"summary": "По лицевому счету", "value": "by_account"},
                                 "by_account_subs_stat_id": {"summary": "По лицевому счету и статусу абонента",
                                                             "value": "by_account_subs_stat_id"},
                                 "by_customer_subs_stat_id": {"summary": "По идентификатору регистрационных данных клиента и статусу абонента",
                                                              "value": "by_customer_subs_stat_id"},
                                 "by_clnt_subs_stat_id": {"summary": "По идентификатору клиента и статусу абонента",
                                                          "value": "by_clnt_subs_stat_id"},
                                 "by_customer_id": {"summary": "По идентификатору регистрационных данных клиента",
                                                    "value": "by_customer_id"}
                             }, description="Входные контракты")):
    params = parameters.copy()
    params['clntId'] = clntId
    params['account'] = account
    params['parentClntId'] = parentClntId
    params['subsStatId'] = subsStatId
    params['customerId'] = customerId
    params['inContractSign'] = inContractSign
    result = methods.get_client_profile(params)
    methods.log_history(request="GetClientProfile", datetime=params['targetDate'])
    return result


# Метод получения дополнительных сведений профиля клиента
@router.get("/get-client-opt")
async def get_client_opt_data(clntId: int = Query(None, description="Идентификатор клиента"),
                              clntFldId: int = Query(None, description="Идентификатор дополнительного поля клиента"),
                              inContractSign: str = Query(examples={
                                  "by_clnt_id": {"summary": "По идентификатору клиента", "value": "by_clnt_id"},
                                  "by_in_fld_id": {"summary": "По идентификатору дополнительного поля клиента",
                                                   "value": "by_in_fld_id"},
                                  "by_out_fld_id": {"summary": "По идентификатору дополнительного поля клиента",
                                                    "value": "by_out_fld_id"},
                              }, description="Входные контракты")):
    params = parameters.copy()
    params['clntId'] = clntId
    params['clntFldId'] = clntFldId
    params['inContractSign'] = inContractSign
    result = methods.get_client_opt_data(params)
    methods.log_history(request="GetClientOptData", datetime=params['targetDate'])
    return result


# Метод изменения дополнительных сведений профиля клиента
@router.put("/set-client-opt")
async def set_client_opt_data(setClientOptData: SetClientOptData):
    params = parameters.copy()
    params['inContractSign'] = 'by_opt_data'
    params['clntId'] = setClientOptData.clntId
    params['clientOptData'] = {
        'clntFldId': setClientOptData.clntFldId,
        'fieldValue': setClientOptData.clntFieldValue
    }
    result = methods.set_client_opt_data(params)
    methods.log_history(request="SetClientOptData", datetime=params['targetDate'])
    return result