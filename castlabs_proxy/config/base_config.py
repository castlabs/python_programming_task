# For demo purposes
# On a real application config files will not be committed

from castlabs_proxy.utils import get_secret

import os

class BaseConfig:
    DEBUG = False
    TESTING = False
    DATABASE_URI = 'sqlite:///:memory:'
    BACKEND_URL = 'https://postman-echo.com/post'

    JWT_ALGORITHM = 'HS256'
