
class NavigationHelper:

    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        wd = self.app.wd
        wd.get(self.app.base_url)

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
