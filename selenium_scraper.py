import datetime

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from configmodule.config import config
from connectors import mysql_connector
from exceptions.exceptions import MissingParamsError, CantAggragateError

from validators.validations import validate_types

TIME_LIMIT = config['aggregation']['website_limit']
SELENIUM_HUB = config['selenium']['selenium_hub']

def fetch_financial_data(pre_last_date, user_id, channel, test=False):
    if (isinstance(pre_last_date,str)):
        pre_last_date = datetime.datetime.strptime(pre_last_date, '%Y-%m-%d %H:%M:%S')
    validate_types(user_id, channel)
    if user_id == '' or channel == '':
        raise MissingParamsError("some or all parameters are missing")
    if ((datetime.datetime.now() - pre_last_date).total_seconds() / 60 / 60 <= float(TIME_LIMIT)):
        raise CantAggragateError("please wait for more than {0} hour between aggregations".format(TIME_LIMIT))
    selenium_hub = SELENIUM_HUB
    driver = webdriver.Remote(command_executor=selenium_hub, desired_capabilities=DesiredCapabilities.CHROME)
    driver.get(channel)
    data = {}
    data['balance'] = driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/div[2]').text
    transactions = []
    webelements = driver.find_elements_by_xpath('/html/body/div/div[3]/div')
    for webelement in webelements:
        try:
            transaction_details = webelement.text.split("\n")
            transaction_data = {}
            for detail in transaction_details:
                detail_key_value = detail.split(":")
                transaction_data[detail_key_value[0]] = detail_key_value[1]
            transactions.append(transaction_data)
        except Exception as e:
            print(e)
    data['transactions'] = transactions
    if not test:
        mysql_connector.insert_financial_data(user_id, channel, datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), data)
    return data




