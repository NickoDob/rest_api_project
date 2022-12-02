import pydantic


# Настройки авторизации и соединения с InvApiCore
class Settings(pydantic.BaseSettings):
    wsdlLink: str = pydantic.Field(env='WSDL_LINK')
    userLogin: str = pydantic.Field(env='USER_LOGIN')
    userPassword: str = pydantic.Field(env='USER_PASSWORD')
    outContractName: str = pydantic.Field(env='OUT_CONTRACT_NAME')
    logs: bool = pydantic.Field(env='LOGS')

    webPort: int = pydantic.Field(env='WEB_PORT')
    serviceName: str = pydantic.Field(env='SERVICE_NAME')

    class Config:
        env_file = ".env"