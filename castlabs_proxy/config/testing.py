# For demo purposes
# On a real application config files will not be committed

from castlabs_proxy.config.base_config import BaseConfig

class TestingConfig(BaseConfig):
    TESTING = True