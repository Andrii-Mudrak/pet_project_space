import pytest
import selenium
from application.api.space_api import SpaceAPI
from config.config import Config

print(Config.base_api_key, Config.base_url, Config.base_api)

@pytest.fixture()
def get_base():
    get_base = SpaceAPI(Config.base_url)