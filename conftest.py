import os
import pytest
import configparser
from methods import from_cache, random_string


@pytest.fixture(scope='session')
def config():

    cfg = configparser.ConfigParser()
    cfg_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.cfg')
    cfg.read(cfg_path)
    return cfg


@pytest.fixture(scope='session')
def responses(config):

    requests_number = 10
    data = []
    with pytest.allure.step('Делаем {} запросов к сервису'.format(requests_number)):

        for i in range(requests_number):
            key = random_string()
            response = from_cache(key, config)
            data.append(response)
    return data
