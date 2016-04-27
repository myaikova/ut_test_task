from fixture.my_helper import Helper
from fixture.counter_helper import CounterHelper
from fixture.list_helper import ListHelper
from selenium import webdriver


class Application:

    def __init__(self, host='https://buggy.auroraplatform.com/', user='maria.yaikova@gmail.com', password='gjvbljh'):
        self.wd = webdriver.Firefox()
        self.host = host
        self.user = user
        self.password = password
        self.my_helper = Helper(self)
        self.counter_helper = CounterHelper(self)
        self.list_helper = ListHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def destroy(self):
        print('Finish test run and destroy webdriver')
        self.wd.quit()
