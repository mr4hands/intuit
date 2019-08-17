import datetime
import unittest

from exceptions.exceptions import CantAggragateError
import api_scraper

last_date = (datetime.datetime.now() - datetime.timedelta(hours=4)).strftime('%Y-%m-%d %H:%M:%S')

class MyTestCase(unittest.TestCase):
    # test with all params
    def test_fetch_transactions_all_params(self):
        results = api_scraper.fetch_financial_data(last_date, user_id="061509949", channel="https://qndxqxuz35.execute-api.us-west-2.amazonaws.com/senior-test", on_demand=True)
        self.assertTrue(type(results) == type([]))
        result = results[0]
        self.assertTrue(result["id"])
        self.assertTrue(result["name"])
        self.assertTrue(result["amount"])
        self.assertTrue(result["description"])

    #test with no params
    def test_fetch_transactions_missing_params(self):
        # no params
        with self.assertRaises(TypeError):
            api_scraper.fetch_financial_data()
        # missing user id
        with self.assertRaises(TypeError):
            api_scraper.fetch_financial_data(last_date=last_date, channel="https://qndxqxuz35.execute-api.us-west-2.amazonaws.com/senior-test", on_demand=True)
        # missing channel
        with self.assertRaises(TypeError):
            api_scraper.fetch_financial_data(last_date=last_date, user_id="061509949", on_demand=True)
        # missing last_date
        with self.assertRaises(TypeError):
            api_scraper.fetch_financial_data(channel="https://qndxqxuz35.execute-api.us-west-2.amazonaws.com/senior-test", user_id="061509949", on_demand=True)
        # missing on_demand
        with self.assertRaises(TypeError):
            api_scraper.fetch_financial_data(last_date=last_date, channel="https://qndxqxuz35.execute-api.us-west-2.amazonaws.com/senior-test", user_id="061509949")

    # test small interval between aggregations
    def test_small_aggregation_interval(self):
        with self.assertRaises(CantAggragateError):
            last_date = datetime.datetime.now()
            api_scraper.fetch_financial_data(pre_last_date=last_date, user_id="061509949",
                                             channel="https://qndxqxuz35.execute-api.us-west-2.amazonaws.com/senior-test",
                                             on_demand=True)

    # test incorrect input
    def test_incorrect_input(self):
        # wrong last_date format
        with self.assertRaises(ValueError):
            api_scraper.fetch_financial_data(pre_last_date="2019", user_id="061509949",
                                             channel="https://qndxqxuz35.execute-api.us-west-2.amazonaws.com/senior-test",
                                             on_demand=True)

        # wrong last_date type
        with self.assertRaises(TypeError):
            api_scraper.fetch_financial_data(pre_last_date=2019, user_id="061509949",
                                             channel="https://qndxqxuz35.execute-api.us-west-2.amazonaws.com/senior-test",
                                             on_demand=True)
        # wrong user_id type
        with self.assertRaises(TypeError):
            api_scraper.fetch_financial_data(pre_last_date=last_date, user_id=61509949,
                                             channel="https://qndxqxuz35.execute-api.us-west-2.amazonaws.com/senior-test",
                                             on_demand=True)
        # wrong channel type
        with self.assertRaises(TypeError):
            api_scraper.fetch_financial_data(pre_last_date=last_date, user_id="061509949",
                                             channel=False,
                                             on_demand=True)

        # wrong on_demand type
        with self.assertRaises(TypeError):
            api_scraper.fetch_financial_data(last_date=last_date, user_id="061509949",
                                             channel="https://qndxqxuz35.execute-api.us-west-2.amazonaws.com/senior-test",
                                             on_demand="sad")

        # invalid url
        with self.assertRaises(Exception):
            api_scraper.fetch_financial_data(pre_last_date=last_date, user_id="061509949",
                                             channel="https://nonexisting.url.com/senior-test",
                                             on_demand=True)

if __name__ == '__main__':
    unittest.main()
