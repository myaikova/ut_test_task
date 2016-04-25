
class Helper:

    def __init__(self, app):
        self.app = app

    def open_url(self, url):
        self.app.wd.get(url)

    def login(self):
        self.open_url(self.app.host + '/login')
        login = 'maria.yaikova@gmail.com'
        password = 'gjvbljh'
        self.fill_field('email', login)
        self.fill_field('password', password)
        self.click_button_xpath('//div/div/form/div[2]/button')

    def logout(self):
        self.click_button_xpath('//header/nav/div/div[2]/ul[2]/li/a')

    def open_home_page(self):
        if not self.app.wd.current_url == self.app.host:
            self.open_url(self.app.host)

    def fill_field(self, field_name, field_text):
        if field_text is not None:
            self.app.wd.find_element_by_name(field_name).click()
            self.app.wd.find_element_by_name(field_name).clear()
            self.app.wd.find_element_by_name(field_name).send_keys(field_text)

    def get_field_val(self, field_name):
        z = self.app.wd.find_element_by_name(field_name)
        return z.get_attribute('value')

    def click_button_name(self, button_name):
        self.app.wd.find_element_by_name(button_name).click()

    def click_button_xpath(self, button_path):
        self.app.wd.find_element_by_xpath(button_path).click()

    def reload_page(self):
        self.app.wd.navigate().refresh()

    def confirm_alert(self):
        self.app.wd.switch_to_alert().accept()

    def decline_alert(self):
        self.app.wd.switch_to_alert().dismiss()