
from gql.transport.requests import RequestsHTTPTransport
from gql import gql, Client


class MetaDataClient:
    def __init__(self, url):

        self._client = Client(
            fetch_schema_from_transport=True,
            transport=RequestsHTTPTransport(
                url=url,
                use_json=True
            ),
        )
        self.is_authenticated = False

    @staticmethod
    def wrap_with(string, tag="\""):
        return tag + string + tag

    def authenticate(username, password):
        query = """
        mutation {
                tokenAuth(username: %s, password: %s) {
                    token
                }
            }
        """ % (wrap_with(username), wrap_with(password))

        resp = self._client.execute(query)

        key = resp["data"]["tokenAuth"]["token"]

        self._client.transport.headers = {'Authorization': 'JWT %s' % key}
