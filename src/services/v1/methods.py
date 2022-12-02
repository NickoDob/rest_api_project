import sys
from lxml import etree
from zeep import Client
from requests import exceptions
from loguru import logger
from zeep.plugins import HistoryPlugin
from config import Settings


config = Settings()

# Методы взаимодействия с InvApiCore
class ClientMethods:
    def __init__(self):
        self.history = HistoryPlugin()
        try:
            self.client = Client(config.wsdlLink, plugins=[self.history])
        except exceptions.ConnectTimeout:
            logger.error('Timeout connection')
            sys.exit()
        except exceptions.ConnectionError:
            logger.exception('Error connection')
            sys.exit()

    def get_subs_profile(self, params):
        try:
            return self.client.service.getSubsProfile(iContract=params)
        except exceptions.RequestException:
            logger.exception('Can`t send requests')

    def get_client_profile(self, params):
        try:
            return self.client.service.getClntProfile(iContract=params)
        except exceptions.RequestException:
            logger.exception('Can`t send requests')

    def get_contract_profile(self, parameters):
        try:
            return self.client.service.getContractProfile(iContract=parameters)
        except exceptions.RequestException:
            logger.exception('Can`t send requests')

    def get_client_opt_data(self, parameters):
        try:
            return self.client.service.getClientOptData(iContract=parameters)
        except exceptions.RequestException:
            logger.exception('Can`t send requests')

    def set_client_opt_data(self, parameters):
        try:
            return self.client.service.setClientOptData(iContract=parameters)
        except exceptions.RequestException:
            logger.exception('Can`t send requests')

    def get_subs_opt_data(self, parameters):
        try:
            return self.client.service.getSubsOptData(iContract=parameters)
        except exceptions.RequestException:
            logger.exception('Can`t send requests')

    def set_subs_opt_data(self, parameters):
        try:
            return self.client.service.setSubsOptData(iContract=parameters)
        except exceptions.RequestException:
            logger.exception('Can`t send requests')

    def log_history(self, request, datetime):
        logger.info("Пользователь: {0}; Запрос: {1}; Дата и время запроса: {2}".format(config.userLogin, request, datetime))
        logger.debug(etree.tostring(self.history.last_received["envelope"], encoding="unicode", pretty_print=True))