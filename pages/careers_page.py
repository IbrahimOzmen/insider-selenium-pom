import time
from pages.base_page import BasePage
from pages.qa_jobs_page import QAJobsPage
from config.locators import CareersPageLocators
from config.config import Config
from utils.logger_config import logger


class CareersPage(BasePage):
    # Expected values for assertions
    expected_career_page_title = "Ready to disrupt? | Insider Careers"
    expected_careers_url_keyword = "/careers/"
    expected_locations_text = "Our Locations"
    expected_teams_text = "See all teams"
    expected_life_at_insider_text = "Life at Insider"
    
    def __init__(self, driver):
        self.locator = CareersPageLocators
        super().__init__(driver)

    def check_page_loaded(self):
        return self.expected_careers_url_keyword in self.get_current_url().lower()

    def verify_location_block(self):
        """Verifies the locations block is present and visible"""
        # Log that we're starting location block verification
        logger.info("Checking locations block...")
        
        self.scroll_to_element(*self.locator.LOCATIONS_BLOCK)
        time.sleep(1)
        
        is_displayed = self.wait_element_visibility(self.locator.LOCATIONS_BLOCK)
        
        if is_displayed:
            # Log successful verification of locations block
            logger.info("Locations block verified successfully")
        else:
            # Log error if locations block is not found
            logger.error("Locations block not found")
            
        return is_displayed

    def get_location_block_text(self):
        return self.get_text(self.locator.LOCATIONS_BLOCK)

    def verify_teams_block(self):
        """Verifies the teams block is present and visible"""
        # Log that we're starting teams block verification
        logger.info("Checking teams block...")
        
        self.scroll_to_element(*self.locator.TEAMS_BLOCK)
        time.sleep(1)
        
        is_displayed = self.wait_element_visibility(self.locator.TEAMS_BLOCK)
        
        if is_displayed:
            # Log successful verification of teams block
            logger.info("Teams block verified successfully")
        else:
            # Log error if teams block is not found
            logger.error("Teams block not found")
            
        return is_displayed

    def get_teams_block_text(self):
        return self.get_text(self.locator.TEAMS_BLOCK)

    def verify_life_at_insider_block(self):
        """Verifies the Life at Insider block is present and visible"""
        # Log that we're starting Life at Insider block verification
        logger.info("Checking Life at Insider block...")
        
        self.scroll_to_element(*self.locator.LIFE_AT_INSIDER_BLOCK)
        time.sleep(1)

        is_displayed = self.wait_element_visibility(self.locator.LIFE_AT_INSIDER_BLOCK)
        
        if is_displayed:
            logger.info("Life at Insider block verified successfully")
        else:
            logger.error("Life at Insider block not found")
            
        return is_displayed

    def get_life_at_insider_block_text(self):
        return self.get_text(self.locator.LIFE_AT_INSIDER_BLOCK)

    def verify_all_blocks(self):
        """Verifies all career page blocks (locations, teams, life at insider)"""
        # Log that we're starting verification of all blocks
        logger.info("Checking all career page blocks...")
        
        locations_ok = self.verify_location_block()
        teams_ok = self.verify_teams_block()
        life_ok = self.verify_life_at_insider_block()
        
        all_ok = locations_ok and teams_ok and life_ok
        
        # Log detailed results for each block verification
        logger.info("Verification Results:")
        logger.info(f"   Locations: {'OK' if locations_ok else 'FAIL'}")
        logger.info(f"   Teams: {'OK' if teams_ok else 'FAIL'}")
        logger.info(f"   Life at Insider: {'OK' if life_ok else 'FAIL'}")

        if all_ok:
            logger.info("All blocks verified successfully!")
        else:
            logger.error("Some blocks failed verification!")
        
        return all_ok

    def navigate_to_qa_jobs(self):
        """Navigates to QA jobs page and returns QAJobsPage instance"""
        # Navigate directly to QA jobs URL from config
        self.go_to_url(Config.QA_JOBS_URL)
        # Return new page object for QA jobs page
        return QAJobsPage(self.driver) 