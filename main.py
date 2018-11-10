#!/usr/bin/env python3

from client.meta_data_client import MetaDataClient

from client.objects import Structure, ObjectInstance


def main():

    # client = MetaDataClient("https://meta-data-api.herokuapp.com/graphql/")
    client = MetaDataClient("http://localhost:8000/graphql/")
    client.authenticate("test", "test1234")

    client.get_user()

    objects = client.get_time_series("activities", "distance", "start_date")


if __name__ == '__main__':
    main()
