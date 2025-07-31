import time


from selenium.common import TimeoutException, ElementClickInterceptedException
from pages.base_page import BasePage
from pages.careers_page import CareersPage
from config.locators import HomePageLocators
from utils.logger_config import logger


class HomePage(BasePage):
    expected_home_page_title = "#1 Leader in Individualized, Cross-Channel CX — Insider"


    def __init__(self, driver):
        self.locator = HomePageLocators
        super().__init__(driver)

    def check_page_loaded(self):
        self.wait_element_to_be_clickable(self.locator.LOGO)
        return self.find_element(*self.locator.LOGO).is_displayed() #checks the visibility of the logo on the home page

    def accept_cookies(self):
        """Accepts cookies if popup is present"""
        try:
            logger.info("Looking for cookie popup...")
            
            # Wait for and click the cookie accept button
            self.click_to_element(*self.locator.ACCEPT_COOKIES_BTN)
            logger.info("Cookies accepted successfully")
            
        except TimeoutException as e:
            logger.warning(f"Cookie popup not found: {str(e)}")

        except ElementClickInterceptedException as e:
            logger.error(f"Cookie button could not be clicked: {str(e)}")

    def navigate_to_careers(self):
        """Navigates to careers page through Company menu hover and click"""
        # Log hovering over Company menu
        logger.info("Hovering over Company menu...")
        self.hover_to_element(*self.locator.COMPANY_MENU)
        time.sleep(0.3) # Short delay to make interactions more visible.
        # without this the method can still perform its actions

        logger.info("Waiting for Careers link...")
        self.click_to_element(*self.locator.CAREERS_LINK)
        time.sleep(0.3) # Short delay to make interactions more visible
        
        logger.info("Clicking on Careers link...")
        logger.info("Successfully navigated to Careers page")
        
        # Return new CareersPage object for subsequent operations
        return CareersPage(self.driver)