
class ListHelper:

    max_list_len = 10

    def __init__(self, app):
        self.app = app

    def get_record_list(self):
        list = []
        for element in self.app.wd.find_elements_by_xpath('//div/div/div/div[2]/ol/li'):
            list.append(element.text[0: -7])
            pass
        return list

    def add_record(self, name):
        self.app.my_helper.fill_field(field_name='title', field_text=name)
        self.app.my_helper.click_button_css('button.btn.btn-success')
        # button.btn.btn-success

    def insure_place_available(self):
        if len(self.app.wd.find_elements_by_xpath('//div/div/div/div[2]/ol/li')) == self.max_list_len:
            self.remove_record()

    def insure_record_exists(self):
        if len(self.app.wd.find_elements_by_xpath('//div/div/div/div[2]/ol/li')) == 0:
            self.add_record('lalala')

    def remove_record(self, num=0):
        elements = self.app.wd.find_elements_by_xpath('//div/div/div/div[2]/ol/li/a')
        if len(elements) <= num:
            raise ValueError("Can't delete element %s from list with %s elements" % (num, len(elements)))
        elements[num].click()
