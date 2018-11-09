from gql.transport.requests import RequestsHTTPTransport
from gql import gql, Client
import requests


class MetaDataClient:
    def __init__(self, url):
        self.url = url
        self._client = Client(
            fetch_schema_from_transport=True,
            transport=RequestsHTTPTransport(
                url=url,
                use_json=True
            ),
        )
        self.headers = {}
        self.is_authenticated = False

    def wrap_with(self, string, tag="\""):
        return tag + string + tag

    def authenticate_gql(self, username, password):
        query = """
        mutation {
                tokenAuth(username: %s, password: %s) {
                    token
                }
            }
        """ % (self.wrap_with(username), self.wrap_with(password))

        resp = self._client.execute(query)

        key = resp["data"]["tokenAuth"]["token"]

        self._client.transport.headers = {'Authorization': 'JWT %s' % key}

    # A simple function to use requests.post to make the API call. Note the json= section.

    def update_token(self, token, token_type="JWT"):
        self.headers["Authorization"] = "%s %s" % (token_type, token)

    def run_query(self, query):
        request = requests.post(self.url,
                                json={'query': query}, headers=self.headers)
        if request.status_code == 200:
            data = request.json()
            if "errors" in data:
                raise Exception(data["errors"])
            else:
                return data
        else:
            raise Exception(request.json())

    def authenticate(self, username, password):

        query = """
            mutation {
                    tokenAuth(username: %s, password: %s) {
                        token
                    }
                }
            """ % (self.wrap_with(username), self.wrap_with(password))

        result = self.run_query(query)  # Execute the query
        token = result["data"]["tokenAuth"]["token"]
        self.update_token(token)

    def get_user(self):
        query = """
        query userqueue{
	
            profile{
                language
                birthdate
                audioThreshold
                user {
                    username
                    email
                    lastName
                    firstName
            }
            }
        }
        """
        result = self.run_query(query)
        print(result)
