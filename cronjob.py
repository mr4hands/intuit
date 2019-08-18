import api_scraper
import selenium_scraper
import statement_handler
from connectors import mysql_connector
from exceptions.exceptions import CantAggragateError


def get_all_user_data():
    all_users = mysql_connector.get_all_users()
    for user in all_users:
        user_id = str(user[0])
        if user_id == '':
            continue
        user_channels = mysql_connector.get_user_channels(user_id=user_id)
        print(user_channels)
        for user_channel in user_channels:
            channel = user_channel[0]
            channel_type = user_channel[1]
            last_aggregation = mysql_connector.get_last_aggregation_for_user_channel(user_id, channel)
            if channel_type == "api":
                try:
                    api_scraper.fetch_financial_data(pre_last_date=last_aggregation, user_id=user_id, channel=channel)
                except CantAggragateError as e:
                    print(e)
            elif channel_type == "website":
                try:
                    selenium_scraper.fetch_financial_data(pre_last_date=last_aggregation, user_id=user_id, channel=channel)
                except CantAggragateError as e:
                    print(e)
        # after getting all channels data, get all statements
        statement_handler.get_statments(user_id)


get_all_user_data()