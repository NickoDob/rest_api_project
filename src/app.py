import uvicorn
import sys
from fastapi import Depends, FastAPI, APIRouter
from loguru import logger
from api.v1 import client, subs, contract
from services.v1.auth import get_current_user
from config import Settings

app = FastAPI()
config = Settings()

# Экземпляр класса APIRouter для создания операций пути
app_router = APIRouter(
    prefix='/api/v1',
    dependencies=[Depends(get_current_user)]
)

# Включение роутеров из подмодулей client, subs и contract
app_router.include_router(client.router)
app_router.include_router(subs.router)
app_router.include_router(contract.router)

# Включение главного роутера
app.include_router(app_router)


@app.get("/")
async def health_check():
    return {'app': 'runing'}


@logger.catch
def main(method=None, obj1=None, obj2=None, obj3=None):
    uvicorn.run(app, port=config.webPort, debug=True)


if __name__ == "__main__":
    main(*sys.argv[1:])