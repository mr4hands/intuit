from flask import Flask, request
import api_scraper
import selenium_scraper
from connectors import mysql_connector

app = Flask(__name__)


@app.route('/api/demand_data/', methods=['post'])
def on_demand_data_aggregation():
    request_json = request.get_json()
    user_id = request_json["user_id"]
    username = request_json["username"]
    last_aggregation = request_json["last_aggregation"]
    channel = request_json["channel"]
    transactions = []
    channel_type = mysql_connector.get_channel_type(channel)
    print(channel_type)
    if channel_type == "api":
        transactions = api_scraper.fetch_financial_data(pre_last_date=last_aggregation, test=True, user_id=user_id, channel=channel)
    elif channel_type == "website":
        transactions = selenium_scraper.fetch_financial_data(pre_last_date=last_aggregation, test=True, user_id=user_id, channel=channel)
#   elif channel_type == "statment":
#TODO
    return str(transactions)

@app.route('/api/get_user_data/', methods=['post'])
def get_user_data():
    request_json = request.get_json()
    user_id = request_json["user_id"]
    username = request_json["username"]
    last_aggregation = request_json["last_aggregation"]
    user_channels = mysql_connector.get_user_channels(user_id)
    response = []
    for user_channel in user_channels:
        channel = user_channel[0]
        channel_type = user_channel[1]
        if channel_type == "api":
            response.append(api_scraper.fetch_financial_data(pre_last_date=last_aggregation, user_id=user_id, channel=channel))
        elif channel_type == "website":
            response.append(selenium_scraper.fetch_financial_data(pre_last_date=last_aggregation, user_id=user_id, channel=channel))
        # TODO statement
    return str(response)
