from fixture.my_helper import Helper
from fixture.counter_helper import CounterHelper
from selenium import webdriver


class Application:

    def __init__(self, host='https://buggy.auroraplatform.com/'):
        self.wd = webdriver.Firefox()
        self.host = host
        self.my_helper = Helper(self)
        self.counter_helper = CounterHelper(self)

    def is_valid(self):
        try:
            self.my_helper.current_url
            return True
        except:
            return False

    def destroy(self):
        print('Finish test run and destroy webdriver')
        self.wd.quit()
