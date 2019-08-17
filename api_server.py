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
        transactions = api_scraper.fetch_transactions(pre_last_date=last_aggregation, on_demand=True, user_id=user_id, channel=channel)
    elif channel_type == "website":
        transactions = selenium_scraper.fetch_transactions(pre_last_date=last_aggregation, on_demand=True, user_id=user_id, channel=channel)
#   elif channel_type == "statment":
#TODO
    return str(transactions)

@app.route('/api/get_user_data/<user_id>', methods=['post'])
def get_user_data(user_id):
    request_json = request.get_json()
    user_id = request_json["user_id"]
    username = request_json["username"]
    last_aggregation = request_json["last_aggregation"]
    user_channels = mysql_connector.get_user_channels(user_id)
    for user_channel in user_channels:
        channel = user_channel[0]
        channel_type = user_channel[1]
        if channel_type == "api":
            api_scraper.fetch_transactions(last_date=last_aggregation, on_demand=True, user_id=user_id, channel=channel)
        elif channel_type == "web":
            api_scraper.fetch_transactions(last_date=last_aggregation, on_demand=True, user_id=user_id, channel=channel)
        # TODO statement