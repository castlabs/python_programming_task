class BaseConfig:
    DEBUG = False
    TESTING = False
    DATABASE_URI = 'sqlite:///:memory:'
    BACKEND_URL = 'https://postman-echo.com/post'

    JWT_TOKEN = 'a9ddbcaba8c0ac1a0a812dc0c2f08514b23f2db0a68343cb8199ebb38a6d91e4ebfb378e22ad39c2d01 d0b4ec9c34aa91056862ddace3fbbd6852ee60c36acbf'
    JWT_ALGORITHM = 'HS256'
