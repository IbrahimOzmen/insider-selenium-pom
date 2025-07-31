import unittest
import sys
import os

# Add the project root to the path so that Python can find the modules
current_dir = os.path.dirname(__file__)  # this line refers to tests/ folder
project_root = os.path.dirname(current_dir)  # parent folder of tests/ (project root)
sys.path.insert(0, project_root) # this line tells python to search for modules in this directory.

from config.locators import QAJobsPageLocators
from tests.base_test import BaseTest
from pages.home_page import HomePage
from config.config import Config
from utils.logger_config import logger


class TestInsider(BaseTest):
    def test_end_to_end_insider_flow(self):
        """End-to-End Test: Complete Insider job application flow from homepage to Lever page"""

        # Step 1: Home Page Verification
        try:
            logger.info("Step 1: Home page verification")
            home_page = HomePage(self.driver)
            home_page.go_to_url(Config.BASE_URL)
            self.soft_assert(self.assertEqual, home_page.get_current_url(), Config.BASE_URL)
            logger.info("Accepted cookies...")
            home_page.accept_cookies()
            self.soft_assert(self.assertTrue, home_page.check_page_loaded(), "Home page is not loaded properly")
            page_title = home_page.get_title()
            self.soft_assert(self.assertEqual, home_page.expected_home_page_title, page_title)
            self.assert_all("Home Page Kontrolleri")
            logger.info("Home page verification successful.")
        except AssertionError as e:
            self.take_screenshot_on_failure("step1_homepage")
            logger.error(f"Step 1 failed: {str(e)}")
            raise

        # Step 2: Careers Page Verification
        try:
            logger.info("Step 2: Careers page verification")
            careers_page = home_page.navigate_to_careers()
            self.soft_assert(self.assertTrue, careers_page.check_page_loaded(), "Careers page is not loaded")
            careers_url = self.driver.current_url
            self.soft_assert(self.assertIn, careers_page.expected_careers_url_keyword, careers_url.lower())
            careers_title = careers_page.get_title()
            self.soft_assert(self.assertIsNotNone, careers_title)
            self.soft_assert(self.assertEqual, careers_page.expected_career_page_title, careers_title)
            locations_ok = careers_page.verify_location_block()
            teams_ok = careers_page.verify_teams_block()
            life_ok = careers_page.verify_life_at_insider_block()
            self.soft_assert(self.assertTrue, locations_ok)
            self.soft_assert(self.assertTrue, teams_ok)
            self.soft_assert(self.assertTrue, life_ok)
            self.soft_assert(self.assertEqual, careers_page.expected_locations_text,
                             careers_page.get_location_block_text())
            self.soft_assert(self.assertEqual, careers_page.expected_teams_text, careers_page.get_teams_block_text())
            self.soft_assert(self.assertEqual, careers_page.expected_life_at_insider_text,
                             careers_page.get_life_at_insider_block_text())
            self.assert_all("Careers Page Kontrolleri")
            logger.info("Careers page verification successful.")
        except AssertionError as e:
            self.take_screenshot_on_failure("step2_careers")
            logger.error(f"Step 2 failed: {str(e)}")
            raise

        # Step 3: QA Jobs Filtering
        try:
            logger.info("Step 3: QA jobs filtering")
            qa_jobs_page = careers_page.navigate_to_qa_jobs()
            self.soft_assert(self.assertTrue, qa_jobs_page.check_page_loaded(), "QA jobs page is not loaded")
            qa_url = self.driver.current_url
            self.soft_assert(self.assertIn, qa_jobs_page.expected_qa_page_url_keyword, qa_url.lower())
            qa_title = qa_jobs_page.get_title()
            self.soft_assert(self.assertIsNotNone, qa_title)
            self.soft_assert(self.assertNotEqual, qa_title, "")
            self.soft_assert(self.assertIn, qa_jobs_page.expected_qa_page_title, qa_title)
            qa_jobs_page.click_see_all_qa_jobs()
            qa_jobs_page.filter_by_location()
            self.assert_all("QA Jobs Filtering")
            logger.info("QA jobs filtering successful.")
        except AssertionError as e:
            self.take_screenshot_on_failure("step3_qajobs")
            logger.error(f"Step 3 failed: {str(e)}")
            raise

        # Step 4: Job Detail Verification
        try:
            logger.info("Step 4: Job details verification")
            job_details_ok = qa_jobs_page.verify_job_details()
            self.soft_assert(self.assertTrue, job_details_ok, "Job details could not be verified!")
            self.assert_all("Job Details Verification")
            logger.info("Job details verification successful.")
        except AssertionError as e:
            self.take_screenshot_on_failure("step4_jobdetails")
            logger.error(f"Step 4 failed: {str(e)}")
            raise

        # Step 5: Lever Redirect and Validation
        try:
            logger.info("Step 5: Lever redirect and validation")
            lever_page = qa_jobs_page.navigate_to_lever_page_for_desired_job_first_job(
                *QAJobsPageLocators.SENIOR_QA_ENGINEER_VIEW_ROLE)
            lever_page_url = lever_page.get_current_url()
            self.soft_assert(self.assertIn, lever_page.expected_lever_page_url, lever_page_url)
            lever_title = lever_page.get_title()
            self.soft_assert(self.assertIsNotNone, lever_title)
            self.soft_assert(self.assertNotEqual, lever_title, "")
            self.soft_assert(self.assertGreater, len(lever_title), 0)
            self.soft_assert(self.assertTrue, lever_page.check_apply_button_is_present(), "Apply button is not present")
            self.assert_all("Lever Page Kontrolleri")
            logger.info("Lever page verification successful.")
            logger.info("END-TO-END TEST COMPLETED SUCCESSFULLY!")

        except AssertionError as e:
            # Take screenshot on failure for debugging
            self.take_screenshot_on_failure("end_to_end")
            logger.error(f"Test failed: {str(e)}")
            raise


if __name__ == "__main__":
    # Run the test class directly when script is executed
    unittest.main(verbosity=2)