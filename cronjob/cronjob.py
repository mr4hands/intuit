import api_scraper
import selenium_scraper
from connectors import mysql_connector


def get_all_user_data():
    all_users = mysql_connector.get_all_users()
    for user_id in all_users:
       channels = mysql_connector.get_user_channels(user_id=user_id)
       for channel in channels:
           last_aggregation = mysql_connector.get_last_aggregation_for_user_channel(user_id,channel)
           api_scraper.fetch_financial_data(pre_last_date=last_aggregation, user_id=user_id, channel=channel)
           selenium_scraper.fetch_financial_data(pre_last_date=last_aggregation, user_id=user_id, channel=channel)