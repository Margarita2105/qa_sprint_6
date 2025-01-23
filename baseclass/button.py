from baseclass.base import Base

class Button(Base):
  #
    def __init__(self, driver):
        self.driver = driver

    def press_button(self, loc, loc_text):

        element = self.driver.find_element(*loc)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.wait(loc)
        element.click()
        self.wait(loc_text)

        return self.driver.current_url

    def press_logo(self, loc, loc_text):

        self.driver.find_element(*loc).click()
        tabs = self.driver.window_handles
        self.driver.switch_to.window(tabs[1])
        self.wait(loc_text)

        return self.driver.current_url
