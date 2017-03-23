from congresso_api.connection import Connection
from unittest import TestCase
import pytest

class Test(TestCase):

    @pytest.fixture(autouse=True)
    def connection(self):
        return Connection()

    def test_perform_request(self):
        connection = Connection()
        self.assertIsInstance(connection.perform_request(url='http://www.google.com'),
                              str)