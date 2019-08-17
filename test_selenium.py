import datetime
import unittest

from exceptions.exceptions import CantAggragateError
import selenium_scraper

last_date = (datetime.datetime.now() - datetime.timedelta(hours=5)).strftime('%Y-%m-%d %H:%M:%S')

class MyTestCase(unittest.TestCase):
    # test with all params
    def test_fetch_transactions_all_params(self):
        results = selenium_scraper.fetch_financial_data(last_date, user_id="061509949",
                                                        channel="https://dratler.github.io/fake-bank/",
                                                        on_demand=True)
        self.assertTrue(type(results) == type([]))
        result = results[0]
        self.assertTrue(result["Id"])
        self.assertTrue(result["Date"])
        self.assertTrue(result["Balance"])
        self.assertTrue(result["Description"])

    # test with no params
    def test_fetch_transactions_missing_params(self):
        # no params
        with self.assertRaises(TypeError):
            selenium_scraper.fetch_financial_data()
        # missing user id
        with self.assertRaises(TypeError):
            selenium_scraper.fetch_financial_data(last_date=last_date,
                                                  channel="https://dratler.github.io/fake-bank/",
                                                  on_demand=True)
        # missing channel
        with self.assertRaises(TypeError):
            selenium_scraper.fetch_financial_data(last_date=last_date, user_id="061509949", on_demand=True)
        # missing last_date
        with self.assertRaises(TypeError):
            selenium_scraper.fetch_financial_data(
                channel="https://qndxqxuz35.execute-api.us-west-2.amazonaws.com/senior-test",
                user_id="061509949", on_demand=True)
        # missing on_demand
        with self.assertRaises(TypeError):
            selenium_scraper.fetch_financial_data(last_date=last_date,
                                                  channel="https://dratler.github.io/fake-bank/",
                                                  user_id="061509949")

    # test small interval between aggregations
    def test_small_aggregation_interval(self):
        last_date = datetime.datetime.now()
        with self.assertRaises(CantAggragateError):
            selenium_scraper.fetch_financial_data(pre_last_date=last_date, user_id="061509949",
                                                  channel="https://dratler.github.io/fake-bank/",
                                                  on_demand=True)

    # test incorrect input
    def test_incorrect_input(self):
        # wrong last_date format
        with self.assertRaises(ValueError):
            selenium_scraper.fetch_financial_data(pre_last_date="2019", user_id="061509949",
                                                  channel="https://dratler.github.io/fake-bank/",
                                                  on_demand=True)
        # wrong last_date type
        with self.assertRaises(TypeError):
            selenium_scraper.fetch_financial_data(pre_last_date=2019, user_id="061509949",
                                                  channel="https://dratler.github.io/fake-bank/",
                                                  on_demand=True)
        # wrong user_id type
        with self.assertRaises(TypeError):
            selenium_scraper.fetch_financial_data(pre_last_date=last_date, user_id=61509949,
                                                  channel="https://dratler.github.io/fake-bank/",
                                                  on_demand=True)
        # wrong channel type
        with self.assertRaises(TypeError):
            selenium_scraper.fetch_financial_data(last_date=last_date, user_id="061509949",
                                                  channel=False,
                                                  on_demand=True)

        # wrong on_demand type
        with self.assertRaises(TypeError):
            selenium_scraper.fetch_financial_data(pre_last_date=last_date, user_id="061509949",
                                                  channel="https://dratler.github.io/fake-bank/",
                                                  on_demand="sad")


if __name__ == '__main__':
    unittest.main()
