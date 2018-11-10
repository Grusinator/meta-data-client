from gql.transport.requests import RequestsHTTPTransport
from gql import gql, Client
import requests

from client.gql_requests.gql_requests import GqlRequests


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

    def replace_args(self, query, **kwargs):
        for key, arg in kwargs.items():
            query = query.replace("{{%s}}" % key, self.wrap_with(arg))
        return query

    def get_user(self):
        query = GqlRequests.get_user_info
        result = self.run_query(query)
        print(result)

    def clean_gql_structure(self, input_data):
        if input_data is None:
            return
        if isinstance(input_data, list):

            cleaned_list = []
            for elm in input_data:
                if isinstance(elm, dict):
                    if "node" in elm.keys():
                        elm = elm["node"]

                elm = self.clean_gql_structure(elm)
                cleaned_list.append(elm)

            return cleaned_list

        elif isinstance(input_data, dict):
            for key, value in input_data.items():

                # if any edges appear skip one level
                if isinstance(value, dict):
                    if "edges" in value.keys():
                        value = value["edges"]
                input_data[key] = self.clean_gql_structure(value)

        return input_data

    def get_time_series(self, object_label, float_label, datetime_label):
        kwargs = dict(locals())
        kwargs.pop("self")
        query = GqlRequests.get_all_instances
        query = self.replace_args(query, **kwargs)
        res = self.run_query(query)
        res = self.clean_gql_structure(res)
        return res
