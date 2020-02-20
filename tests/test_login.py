import unittest

from metadataclient.gql_requests.user import get_dummy_user
from metadataclient.meta_data_client import MetaDataClient
from load_env import *


class TestLoginMethod(unittest.TestCase):

    def test_login(self):
        client = MetaDataClient(GRAPHQL_URL)
        client.authenticate(WEB_USERNAME, WEB_PASSWORD)
        self.assertIsNotNone(client._client.transport.headers)

    def test_get_user_info(self):
        client = MetaDataClient(GRAPHQL_URL)
        client.authenticate(WEB_USERNAME, WEB_PASSWORD)
        user = client.get_user()
        expected = {'user': {'email': 'grusinator@gmail.com',
                             'firstName': 'William',
                             'lastName': 'Hansen',
                             'username': 'grusinator'}}
        self.assertEqual(user, expected)

    def test_get_dummy_user(self):
        client = MetaDataClient(GRAPHQL_URL)
        client.authenticate(WEB_USERNAME, WEB_PASSWORD)
        user = client.run_query(get_dummy_user)
        expected = {'dummy': {'firstName': 'peter', 'lastName': 'larsen'}}
        self.assertEqual(user, expected)
