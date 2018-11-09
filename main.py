#!/usr/bin/env python3

from client.meta_data_client import MetaDataClient


def main():
    client = MetaDataClient("https://meta-data-api.herokuapp.com/graphql/")
    client.authenticate("test", "test1234")

    client.get_user()


if __name__ == '__main__':
    main()
