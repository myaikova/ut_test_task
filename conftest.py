import pytest
from fixture.application import Application
import json
import os.path as path

fixture = None
config_data = None

@pytest.fixture
def app(request):
    global fixture
    global config_data
    if config_data is None:
        config_path = path.join(path.dirname(path.abspath(__file__)), request.config.getoption("--config"))
        with open(config_path) as config_file:
            config_data = json.load(config_file)
    if fixture is None or not fixture.is_valid():
        instance = request.config.getoption("--instance")
        check_instance(instance)
        fixture = Application(host=config_data[instance].get('host'))
        fixture.my_helper.open_home_page()
        fixture.my_helper.login()
    return fixture


def check_instance(instance):
    global config_data
    if instance in config_data:
        return True
    else:
        raise ValueError('Unknown instance name in config file!')


@pytest.fixture(scope='session', autouse=True)
def finish(request):
    def fin():
        fixture.my_helper.logout()
        fixture.destroy()
        print('Finish test session')
    request.addfinalizer(fin)


def pytest_addoption(parser):
    parser.addoption("--config", action="store", default='config.json')
    parser.addoption("--instance", action="store", default='live')
