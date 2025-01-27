from base_pages.base_page import BasePage

class ButtonPage(BasePage):

    def __init__(self, driver):
        BasePage.__init__(self, driver)

    def press_button(self, locator, locator_text):

        element = self.find_element_on_page(locator)
        self.scroll(element)
        self.wait_visibility_of_element(locator)
        element.click()
        self.wait_visibility_of_element(locator_text)

        return self.current_urls()

    def press_logo(self, locator, locator_text):
        self.click_on_element(locator)
        self.get_tab_and_switch()
        self.wait_visibility_of_element(locator_text)

        return self.current_urls()
