from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from config.config import Config


class BasePage:
    """Base page class that provides common functionality for all page objects. The class inherited from this class
    will have all the methods below"""
    def __init__(self, driver):
        # Initialize base page with WebDriver and configuration
        self.base_url = Config.BASE_URL
        self.driver = driver
        # Set timeout for explicit waits from configuration
        self.timeout = Config.EXPLICIT_WAIT
        # Create WebDriverWait instance for explicit waiting
        self.wait= WebDriverWait(self.driver, self.timeout)

    def find_element(self, *locator):
        """Finds a single element using the provided locator"""
        # Use WebDriver to find element with given locator strategy
        return self.driver.find_element(*locator)

    def click_to_element(self, *locator):
        """Waits for element to be clickable and then clicks it"""
        # Wait for element to be clickable before clicking to avoid errors
        self.wait_element_to_be_clickable(locator).click()

    def find_elements(self, *locator):
        """Finds multiple elements using the provided locator"""
        # Use WebDriver to find all matching elements
        return self.driver.find_elements(*locator)

    def go_to_url(self, url):
        """Navigates to the given URL"""
        # Navigate to the specified URL using WebDriver
        self.driver.get(url)

    def get_title(self):
        return self.driver.title

    def get_current_url(self):
        """Returns the current page's URL"""
        # Get the current URL from the browser
        return self.driver.current_url

    def hover_to_element(self, *locator):
        """Hovers over the specified element"""
        # Find the element to hover over
        element = self.find_element(*locator)
        # Create action chain to perform hover action
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()

    def wait_element_to_be_clickable(self, locator):
        return self.wait.until(ec.element_to_be_clickable(locator))

    def wait_element_visibility(self, locator):
        return self.wait.until(ec.visibility_of_element_located(locator))

    def get_text(self, locator):
        return self.wait_element_to_be_clickable(locator).text

    def switch_to_window(self, index: int = -1):
        """Switches to the window at the specified index. By default, switches to the last opened window."""
        # Switch to window using window handles array - negative index gets last window
        self.driver.switch_to.window(self.driver.window_handles[index])

    def get_window_count(self) -> int:
        """Returns the total number of open tabs in the browser."""
        # Count the number of window handles (tabs/windows)
        return len(self.driver.window_handles)

    def scroll_down(self, pixels=500):
        """Scrolls the page down by the specified number of pixels"""
        # Execute JavaScript to scroll the page vertically
        self.driver.execute_script(f"window.scrollBy(0, {pixels});")

    def scroll_to_element(self, *locator):
        """Scrolls to the specified element"""
        # Find the target element
        element = self.find_element(*locator)
        # Execute JavaScript to smoothly scroll element into center of view
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)
