import datetime
from fastapi import APIRouter
from fastapi import Query
from config import Settings
from services.v1.methods import ClientMethods

methods = ClientMethods()
config = Settings()

# Экземпляр класса APIRouter для создания операций пути
router = APIRouter(
    prefix='/contract',
    tags=["Contract"],
)

# Параметры для подключения методов к InvApiCore
parameters = {
        'outContractName': config.outContractName,
        'userLogin': config.userLogin,
        'targetDate': datetime.datetime.now().isoformat(),
        }


#Метод получения информации о профиле контракта
@router.get("/contract-profile")
async def get_contract_profile(clntId: int = Query(None, description="Идентификатор клиента"),
                               contractNum: int = Query(None, description="Номер контракта"),
                               name: str = Query(None, description="Имя контракта"),
                               inContractSign: str = Query(examples={
                                   "by_clnt_id": {"summary": "По идентификатору клиента", "value": "by_clnt_id"},
                                   "by_contract": {"summary": "По номеру контракта", "value": "by_contract"},
                                   "by_contract_name": {"summary": "По имени контракта", "value": "by_contract_name"},
                               }, description="Входные контракты")):
    params = parameters.copy()
    params['clntId'] = clntId
    params['contractNum'] = contractNum
    params['name'] = name
    params['inContractSign'] = inContractSign
    result = methods.get_contract_profile(params)
    methods.log_history(request="GetContractProfile", datetime=params['targetDate'])
    return result