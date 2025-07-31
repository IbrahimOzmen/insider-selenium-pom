import time
from pages.base_page import BasePage
from config.locators import QAJobsPageLocators
from pages.jobs_lever_page import JobsLeverPage
from utils.logger_config import logger

class QAJobsPage(BasePage):
    # Expected values for assertions
    expected_qa_page_title = "Insider quality assurance job opportunities"
    expected_qa_page_url_keyword = "/quality-assurance/"
    expected_position_title = "Quality Assurance"
    expected_position_department = "Quality Assurance"
    expected_position_location = "Istanbul, Turkiye"

    
    def __init__(self, driver):
        self.locator = QAJobsPageLocators
        super().__init__(driver)

    def check_page_loaded(self):
        return self.expected_qa_page_url_keyword in self.get_current_url().lower()

    def click_see_all_qa_jobs(self):
        """Scrolls to and clicks the 'See all QA jobs' button"""
        # Scroll to the 'See all QA jobs' button for better visibility
        self.scroll_to_element(*self.locator.SEE_ALL_QA_JOBS_BTN)
        self.click_to_element(*self.locator.SEE_ALL_QA_JOBS_BTN)
        logger.info("Clicked 'See all QA jobs' button")

    def wait_for_department_to_load(self):
        """Waits for department filter to load and become visible"""
        # Wait for department filter element to be visible before proceeding
        self.wait_element_visibility(self.locator.DEPARTMENT_VALUE_FOR_JOB_FILTERING)
        logger.info("Department filter loaded: Quality Assurance is visible.")

    def filter_by_location(self):
        """Applies location filter to show only Istanbul jobs"""
        # Log that we're starting location filtering process
        logger.info("Applying location filter...")

        # Scroll to location dropdown to ensure it's visible
        self.scroll_to_element(*self.locator.LOCATION_FILTER)
        # Wait for department filter to load first
        # Since we are already on the quality assurance page, we don't need to filter again for the department;
        #  it happens automatically. We just need to wait for the location filters to load.
        #  That's why this method was called here.
        self.wait_for_department_to_load()
        # Click on location dropdown to open the options
        self.click_to_element(*self.locator.LOCATION_FILTER)
        logger.info("Location dropdown opened")
        
        # Click on Istanbul option from the dropdown
        self.click_to_element(*self.locator.ISTANBUL_OPTION)
        logger.info("Istanbul, Turkiye selected")

        logger.info("Location filter applied successfully")
        
        # Scroll down to make job listings visible
        self.scroll_down(400)
        logger.info("Scrolled to job listings section")

    def verify_job_details(self):
        """Verifies job details (position, department, location) for all job listings"""
        # Log that we're starting job details verification
        logger.info("Verifying job details...")
        time.sleep(5)
        self.wait_element_visibility(self.locator.JOB_POSITION) #this refers to all job positions. it could be more than one

        positions = self.find_elements(*self.locator.JOB_POSITION)
        departments = self.find_elements(*self.locator.JOB_DEPARTMENT)
        locations = self.find_elements(*self.locator.JOB_LOCATION)

        if len(positions) == 0:
            # Log warning if no job listings are found
            logger.warning("No job listings found!")
            return False

        if not (len(positions) == len(departments) == len(locations)):
            # Log error if the number of position/department/location element numbers don't match
            logger.error("Job listing element counts don't match!")
            return False

        content_ok = True
        for i in range(len(positions)):
            pos = positions[i].text.strip()
            dep = departments[i].text.strip()
            loc = locations[i].text.strip()

            if self.expected_position_title.lower() not in pos.lower():
                # Log error if position title doesn't contain expected text
                logger.error(f"[Position {i + 1}] '{pos}' should contain '{self.expected_position_title}'.")
                content_ok = False
            if self.expected_position_department != dep:
                # Log error if department doesn't match expected value
                logger.error(f"[Department {i + 1}] Expected: '{self.expected_position_department}', Actual: '{dep}'")
                content_ok = False
            if self.expected_position_location != loc:
                # Log error if location doesn't match expected value
                logger.error(f"[Location {i + 1}] Expected: '{self.expected_position_location}', Actual: '{loc}'")
                content_ok = False

        if content_ok:
            # Log success message with count of verified job listings
            logger.info(f"{len(positions)} job listings verified successfully")
        else:
            # Log warning if some job listings failed verification
            logger.warning("Some job listings could not be verified")

        return content_ok

    def navigate_to_lever_page_for_desired_job_first_job(self, *locator):
        """Navigates to Lever job application page by clicking on 'View Role' button"""
        #I have defined a parameter so that we can provide the locator for the job position you want.
        # We can call this in the test section according to the job we want.

        self.click_to_element(*locator)

        # Switch to the newly opened window (Lever page opens in new tab)
        self.switch_to_window()  # This method switches to the last opened window as default
        logger.info("Switched to new Lever tab.")
        time.sleep(3)  # Wait for page to fully load

        # Create and return JobsLeverPage object for further operations
        return JobsLeverPage(self.driver)