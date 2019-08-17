# importing the requests library
import datetime
import requests
from concurrent.futures import ThreadPoolExecutor as PoolExecutor

from configmodule.config import config
from connectors import mysql_connector
from exceptions.exceptions import MissingParamsError, CantAggragateError
from validators.validations import validate_types

TIME_LIMIT = config['aggregation']['api_limit']

def fetch_financial_data(pre_last_date, user_id, channel, on_demand):
    if (isinstance(pre_last_date,str)):
        pre_last_date = datetime.datetime.strptime(pre_last_date, '%Y-%m-%d %H:%M:%S')
    validate_types(user_id, channel, on_demand)
    if user_id == '' or channel == '':
        raise MissingParamsError("some or all parameters are missing")
    if ((datetime.datetime.now() - pre_last_date).total_seconds() / 60 / 60 <= float(TIME_LIMIT)):
        raise CantAggragateError("please wait for more than {0} hour between aggregations".format("TIME_LIMIT"))
    # running with concurrent connections
    with PoolExecutor(max_workers=20) as executor:
        for response in executor.map(requests.get(url=channel)):
            data = response.json()
            parsed_response = {'balance': data['body']['balance'], 'transactions': data['body']['transactions']}
    if on_demand:
        return parsed_response
    else:
        mysql_connector.set_api_transactions(user_id, response)





