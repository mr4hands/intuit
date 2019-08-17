import datetime
import unittest

from exceptions.exceptions import CantAggragateError
import selenium_scraper

last_date = (datetime.datetime.now() - datetime.timedelta(hours=4)).strftime('%Y-%m-%d %H:%M:%S')

class MyTestCase(unittest.TestCase):
    # test with all params
    def test_fetch_transactions_all_params(self):
        results = selenium_scraper.fetch_financial_data(last_date, user_id="061509949",
                                                        channel="https://dratler.github.io/fake-bank/",
                                                        test=True)
        self.assertTrue(type(results) == type({}))
        self.assertTrue(results.get('balance'))
        self.assertTrue(results.get('transactions'))

    # test with no params
    def test_fetch_transactions_missing_params(self):
        # no params
        with self.assertRaises(TypeError):
            selenium_scraper.fetch_financial_data()
        # missing user id
        with self.assertRaises(TypeError):
            selenium_scraper.fetch_financial_data(last_date=last_date,
                                                  channel="https://dratler.github.io/fake-bank/",
                                                  test=True)
        # missing channel
        with self.assertRaises(TypeError):
            selenium_scraper.fetch_financial_data(last_date=last_date, user_id="061509949", test=True)
        # missing last_date
        with self.assertRaises(TypeError):
            selenium_scraper.fetch_financial_data(
                channel="https://qndxqxuz35.execute-api.us-west-2.amazonaws.com/senior-test",
                user_id="061509949", test=True)

        # missing test
        with self.assertRaises(TypeError):
            selenium_scraper.fetch_financial_data(pre_last_date=last_date, user_id="061509949",
                                                  channel="https://dratler.github.io/fake-bank/",
                                                  test=True)

    # test small interval between aggregations
    def test_small_aggregation_interval(self):
        last_date = datetime.datetime.now()
        with self.assertRaises(CantAggragateError):
            selenium_scraper.fetch_financial_data(pre_last_date=last_date, user_id="061509949",
                                                  channel="https://dratler.github.io/fake-bank/",
                                                  test=True)

    # test incorrect input
    def test_incorrect_input(self):
        # wrong last_date format
        with self.assertRaises(ValueError):
            selenium_scraper.fetch_financial_data(pre_last_date="2019", user_id="061509949",
                                                  channel="https://dratler.github.io/fake-bank/",
                                                  test=True)
        # wrong last_date type
        with self.assertRaises(TypeError):
            selenium_scraper.fetch_financial_data(pre_last_date=2019, user_id="061509949",
                                                  channel="https://dratler.github.io/fake-bank/",
                                                  test=True)
        # wrong user_id type
        with self.assertRaises(TypeError):
            selenium_scraper.fetch_financial_data(pre_last_date=last_date, user_id=61509949,
                                                  channel="https://dratler.github.io/fake-bank/",
                                                  test=True)
        # wrong channel type
        with self.assertRaises(TypeError):
            selenium_scraper.fetch_financial_data(last_date=last_date, user_id="061509949",
                                                  channel=False,
                                                  test=True)



if __name__ == '__main__':
    unittest.main()
