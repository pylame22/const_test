import os

from dotenv import load_dotenv

load_dotenv()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ENV = os.environ['ENV']

# ROUTE
API_PREFIX = '/api'

# FASTAPI
PROJECT_NAME = 'const_test'
DEBUG = bool(int(os.environ['DEBUG']))

# DATABASE
POSTGRES_USER = os.environ['POSTGRES_USER']
POSTGRES_PASSWORD = os.environ['POSTGRES_PASSWORD']
POSTGRES_HOST = os.environ['POSTGRES_HOST']
POSTGRES_PORT = int(os.environ['POSTGRES_PORT'])
POSTGRES_DB = os.environ['POSTGRES_DB']
POSTGRES_MIN_CONNECTIONS_SIZE = int(os.environ['POSTGRES_MIN_CONNECTIONS_SIZE'])
POSTGRES_MAX_CONNECTIONS_SIZE = int(os.environ['POSTGRES_MAX_CONNECTIONS_SIZE'])
POSTGRES_URL = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}'

# SHORTIFY
SHORT_HOST = 'http://const.com/'
