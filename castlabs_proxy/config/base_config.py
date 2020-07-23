# For demo purposes
# On a real application config files will not be committed

import os

class BaseConfig:
    DEBUG = False
    TESTING = False
    DATABASE_URI = 'sqlite:///:memory:'
    BACKEND_URL = 'https://postman-echo.com/post'

    JWT_TOKEN = os.environ['JWT_TOKEN']
    JWT_ALGORITHM = 'HS256'
