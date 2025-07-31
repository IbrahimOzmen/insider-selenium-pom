import os
from datetime import datetime
from config.config import Config
from utils.logger_config import logger


def get_timestamp():
    """Returns formatted timestamp for file naming"""
    # Generate timestamp in YYYYMMDD_HHMMSS format
    return datetime.now().strftime("%Y%m%d_%H%M%S")


class ScreenshotManager:
    def __init__(self, driver):
        self.driver = driver
        self.config = Config()
        self._create_screenshot_dir()

    def _create_screenshot_dir(self):
        """Creates screenshot directory if it doesn't exist"""
        if not os.path.exists(self.config.SCREENSHOT_PATH):
            # Create directory structure for storing screenshots
            os.makedirs(self.config.SCREENSHOT_PATH)

    def take_screenshot(self, name="screenshot"): #default name is screenshot
        """Takes screenshot and saves it with timestamp"""
        # Skip screenshot if disabled in configuration
        if not self.config.SCREENSHOT_ENABLED:
            return None

        timestamp = get_timestamp()
        filename = f"{name}_{timestamp}.png"
        filepath = os.path.join(self.config.SCREENSHOT_PATH, filename)

        try:
            # Capture and save screenshot to specified file path
            self.driver.save_screenshot(filepath)
            return filepath
        except Exception as e:
            # Log error if screenshot capture fails
            logger.error(f"Error taking screenshot: {e}")
            return None

