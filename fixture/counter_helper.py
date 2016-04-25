
class CounterHelper:
    def __init__(self, app):
        self.app = app

    def get_val(self):
        return self.app.wd.find_element_by_id('counter_value').text

    def increase(self):
        self.app.my_helper.click_button_xpath('//div/div/div/div[1]/form/button')
        #//div/div/div/div[1]/form/button