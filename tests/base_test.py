import unittest
import time
import softest
from utils.driver_manager import DriverManager
from utils.screenshot_manager import ScreenshotManager
from utils.logger_config import logger


class BaseTest(softest.TestCase, unittest.TestCase):
    """
    Simple base class for single test method with common setup and teardown
    """

    def setUp(self):
        """Runs before each test method starts"""

        logger.info("STARTING INSIDER TEST AUTOMATION")

        # Record test start time for duration calculation
        self.start_time = time.time()

        # Initialize WebDriver
        logger.info("Starting WebDriver...")
        self.driver_manager = DriverManager()
        self.driver = self.driver_manager.create_driver()

        # Initialize screenshot manager for capturing test evidence
        ScreenshotManager(self.driver)

        logger.info("WebDriver started successfully!")

    def tearDown(self):
        """Runs after each test method completes"""
        # Close WebDriver and clean up resources
        logger.info("Closing WebDriver...")
        if hasattr(self, 'driver_manager') and self.driver_manager:
            self.driver_manager.close_driver()
            logger.info("WebDriver closed successfully")

        # Calculate and log test execution time
        if hasattr(self, 'start_time'):
            end_time = time.time()
            duration = end_time - self.start_time
            logger.info(f"TEST AUTOMATION COMPLETED - Duration: {duration:.2f} seconds")

    def take_screenshot_on_failure(self, test_name):
        """Takes screenshot when test fails for debugging purposes"""
        if hasattr(self, 'driver') and self.driver:
            # Capture screenshot with failure indication in filename
            ScreenshotManager(self.driver).take_screenshot(f"{test_name}_failed")
            logger.info(f"Failure screenshot captured: {test_name}_failed")