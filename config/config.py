import os


class Config:
    """Configuration class containing all application settings and constants"""
    # Browser configuration - supports 'chrome' and 'firefox'
    BROWSER = "firefox"
    # Run browser in headless mode (without UI) if True
    HEADLESS = False

    # Application URLs for testing
    BASE_URL = "https://useinsider.com/"
    QA_JOBS_URL = "https://useinsider.com/careers/quality-assurance/"
    # Timeout configurations in seconds
    IMPLICIT_WAIT = 15  # Global implicit wait for element finding
    EXPLICIT_WAIT = 30  # Explicit wait for specific conditions


    # Screenshot capture configuration
    SCREENSHOT_ENABLED = True
    # Get main project root directory (InsiderFinalProject)
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Directory path for saving screenshots
    SCREENSHOT_PATH = os.path.join(BASE_DIR, "reports", "screenshots")
    # Directory path for saving HTML test reports
    HTML_REPORT_PATH = os.path.join(BASE_DIR, "reports", "html")


