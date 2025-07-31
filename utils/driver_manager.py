from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions

from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions


from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


from config.config import Config

def _setup_common_options(options):
    """Common browser options configuration for Chrome"""
    # Disable sandbox for compatibility in various environments
    options.add_argument("--no-sandbox")
    # Disable shared memory usage for stability
    options.add_argument("--disable-dev-shm-usage")
    # Disable GPU acceleration
    options.add_argument("--disable-gpu")
    # Disable browser extensions
    options.add_argument("--disable-extensions")
    # Disable popup blocking
    options.add_argument("--disable-popup-blocking")
    # Disable browser notifications
    options.add_experimental_option("prefs", {
        "profile.default_content_setting_values.notifications": 2
    })

class DriverManager:
    def __init__(self, headless=Config.HEADLESS, implicit_wait=Config.IMPLICIT_WAIT):
        self.headless = headless
        self.implicit_wait = implicit_wait
        self.driver = None


    def create_driver(self):
        if self.driver is None:
            browser = Config.BROWSER.lower()
            if browser == 'chrome':
                self.driver = self._create_chrome_driver()
            elif browser == 'firefox':
                self.driver = self._create_firefox_driver()
            else:
                # Raise error for unsupported browser types
                raise ValueError(f"Unsupported browser: {browser}. Supported browsers: chrome, firefox")

            self.driver.implicitly_wait(self.implicit_wait)
            if not self.headless:
                self.driver.maximize_window()

        return self.driver

    def _create_chrome_driver(self):
        options = ChromeOptions()
        _setup_common_options(options)

        if self.headless:
            options.add_argument("--headless=new")
        options.add_argument("--window-size=1920,1080")

        return webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=options
        )

    def _create_firefox_driver(self):
        options = FirefoxOptions()

        # Basic Firefox configuration options
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        # Disable web notifications in Firefox
        options.set_preference("dom.webnotifications.enabled", False)
        # Disable push notifications in Firefox
        options.set_preference("dom.push.enabled", False)

        if self.headless:
            options.add_argument("--headless")
        options.add_argument("--width=1920")
        options.add_argument("--height=1080")

        return webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install()),
            options=options
        )

    def close_driver(self):
        """Closes the WebDriver and cleans up resources"""
        if self.driver:
            # Quit the driver and close all browser windows
            self.driver.quit()
            # Set driver to None to prevent reuse
            self.driver = None