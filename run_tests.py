import unittest
from HtmlTestRunner import HTMLTestRunner
import os

from config.config import Config

if __name__ == '__main__':
    # Create a reports folder if one does not already exist.
    report_dir = Config.HTML_REPORT_PATH
    os.makedirs(report_dir, exist_ok=True)

    # Find all tests in the tests/ folder
    loader = unittest.TestLoader()
    suite = loader.discover(start_dir="tests", pattern="test_*.py")

    # Start the HTML reporter
    runner = HTMLTestRunner(
        output=report_dir,
        report_name="InsiderTestReport",       # Raporun dosya adı
        combine_reports=True,                  # Tek sayfa rapor
        add_timestamp=True                     # Zaman damgası eklensin mi
    )
    runner.run(suite)
