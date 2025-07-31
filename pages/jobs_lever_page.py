from config.locators import JobsLeverPageLocators
from pages.base_page import BasePage
from utils.logger_config import logger


class JobsLeverPage(BasePage):
    expected_lever_page_url = "jobs.lever.co"

    def __init__(self, driver):
        self.locator = JobsLeverPageLocators
        super().__init__(driver)


    def check_apply_button_is_present(self):
        self.wait_element_to_be_clickable(self.locator.APPLY_BUTTON)
        return self.find_element(*self.locator.APPLY_BUTTON).is_displayed() #ok