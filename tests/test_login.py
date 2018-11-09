import unittest
from .client import MetaDataClient


class TestLoginMethod(unittest.TestCase):

    def test_upper(self):

        client = MetaDataClient("https://meta-data-api.herokuapp.com/graphql")
        client.authenticate("test", "test1234")

        self.assertIsNotNone(client._client.transport.headers)
