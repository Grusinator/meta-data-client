# settings.py
import os
from os.path import join, dirname
from dotenv import load_dotenv


def load_env():
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)


load_env()
WEB_USERNAME = os.environ.get("WEB_USERNAME")
WEB_PASSWORD = os.environ.get("WEB_PASSWORD")
GRAPHQL_URL = os.environ.get("GRAPHQL_URL")
