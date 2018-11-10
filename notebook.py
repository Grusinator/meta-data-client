# %%
from client.meta_data_client import MetaDataClient

cli = MetaDataClient("https://meta-data-api.herokuapp.com/graphql/")
cli.authenticate("test", "test1234")

cli.get_user()

cli.get_time_series()
