
class LoginHelper:
    def __init__(self, app):
        self.app = app

    def is_logged_as(self, name):
        if self.app.wd.find_element_by_xpath('//div/div[1]/form/b') == '(' + name + ')':
            return True
        else:
            return False

    def login(self, login, pwd):
        self.app.wd.find_element_by_name("user").click()
        self.app.wd.find_element_by_name("user").clear()
        self.app.wd.find_element_by_name("user").send_keys(login)
        self.app.wd.find_element_by_name("pass").click()
        self.app.wd.find_element_by_name("pass").clear()
        self.app.wd.find_element_by_name("pass").send_keys(pwd)
        self.app.wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def ensure_logout(self):
        if self.is_logged():
            self.logout()

    def is_logged(self):
        return len(self.app.wd.find_elements_by_link_text("Logout")) > 0

    def logout(self):
        self.app.wd.find_element_by_link_text("Logout").click()