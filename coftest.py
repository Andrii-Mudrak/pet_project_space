import pytest
import selenium
from application.api.space_api import SpaceAPI
from config.config import Config

@pytest.fixture()
def get_base():
    get_base = SpaceAPI(Config.base_url)