import pytest
from fixture.application import Application

fixture = None


@pytest.fixture
def app(request):
    global fixture
    if fixture is None:
        print('create new fixture')
        fixture = Application()
        fixture.my_helper.open_home_page()
        fixture.my_helper.login()
    else:
        if not fixture.is_valid():
            print('rebuild broken fixture')
            fixture = Application()
            fixture.my_helper.open_home_page()
            fixture.my_helper.login()
    return fixture

'''
@pytest.fixture
def group(request):
    global fixture
    fixture.group_helper.open_group_page()


@pytest.fixture
def contact(request):
    global fixture
    fixture.wd_helper.open_home_page()
'''

@pytest.fixture(scope='session', autouse=True)
def finish(request):
    def fin():
        fixture.my_helper.logout()
        fixture.destroy()
        print('Finish test session')
    request.addfinalizer(fin)
