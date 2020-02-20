from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport

from metadataclient import gql_requests


class MetaDataClient:
    def __init__(self, url):
        self.url = url
        self._client = Client(
            fetch_schema_from_transport=True,
            transport=RequestsHTTPTransport(
                url=url,
                use_json=True,
                headers={},
            ),
        )

    def authenticate(self, username, password):
        variable_values = {"username": username, "password": password}
        resp = self.run_query(gql_requests.authorize, variable_values=variable_values)
        key = resp["tokenAuth"]["token"]
        self.set_auth_token(key)

    def run_query(self, query, variable_values=()):
        query = gql(query) if isinstance(query, str) else query
        resp = self._client.execute(query, variable_values=variable_values)
        self.handle_errors(resp)
        return resp

    def handle_errors(self, resp):
        if "errors" in resp:
            raise Exception(resp["errors"])

    def set_auth_token(self, token, token_type="JWT"):
        self._client.transport.headers = {"Authorization": f"{token_type} {token}"}
        # self._client.transport.headers["Authorization"] = f"{token_type} {token}"

    def get_user(self):
        result = self.run_query(gql_requests.get_user)
        return result

    def get_schema(self):
        result = self.run_query(gql_requests.get_user)
