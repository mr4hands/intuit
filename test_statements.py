import unittest

import statement_handler


class MyTestCase(unittest.TestCase):
    def test_statement(self):
        self.assertTrue(statement_handler.get_statments("061509949"))


if __name__ == '__main__':
    unittest.main()
