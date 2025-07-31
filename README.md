# Insider Test Automation Framework

![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)
![Selenium](https://img.shields.io/badge/selenium-4.34.2-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

A comprehensive Selenium-based test automation framework for testing [Insider](https://useinsider.com/) company's careers page functionality using Page Object Model design pattern.

## Table of Contents

- [Quick Start](#quick-start)
- [Test Scenarios](#test-scenarios)  
- [Technology Stack](#technology-stack)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Page Object Model](#page-object-model)
- [Reporting](#reporting)
- [Troubleshooting](#troubleshooting)

## Quick Start

```bash
# Clone and run in 3 commands
git clone <repository-url>
cd insider-selenium-pom
pip install -r requirements.txt && python run_tests.py
```

## Test Scenarios

This framework automates the following end-to-end test scenario:

1. **Home Page Validation** - Loading and validation of Insider's home page
2. **Careers Page Verification** - Validation of careers page sections (Locations, Teams, Life at Insider)
3. **QA Jobs Filtering** - Filtering quality assurance jobs by Istanbul location
4. **Job Details Verification** - Validation of job positions, departments, and location information
5. **Lever Page Redirection** - Redirection to job application page (Lever) and validation

## Technology Stack

| Technology | Version | Description |
|-----------|----------|-------------|
| Python | 3.8+ | Main programming language |
| Selenium WebDriver | 4.34.2 | Web browser automation |
| WebDriver Manager | 4.0.2 | Automatic driver management |
| HTMLTestRunner | 1.2.1 | HTML test reports |
| SofTest | 1.2.0.0 | Soft assertion support |

## Installation

### Prerequisites

| Requirement | Version | Check Command |
|-------------|---------|---------------|
| Python | 3.8+ | `python --version` |
| Git | Latest | `git --version` |
| Chrome/Firefox | Latest | Browser settings > About |

### Setup Steps

1. **Clone the repository**
```bash
git clone <repository-url>
cd insider-selenium-pom
```

2. **Create virtual environment (recommended)**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux  
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

**Note:** WebDriver Manager automatically downloads required drivers. No manual installation needed.

## Configuration

Configuration file: `config/config.py`

```python
class Config:
    BROWSER = "chrome"              # "chrome" or "firefox"
    HEADLESS = False               # True for headless mode
    BASE_URL = "https://useinsider.com/"
    IMPLICIT_WAIT = 15             # Seconds
    EXPLICIT_WAIT = 30             # Seconds
    SCREENSHOT_ENABLED = True      # Capture screenshots on failure
```

## Usage

### Run All Tests
```bash
python run_tests.py
```

### Run Single Test
```bash
python -m unittest tests/test_insider.py -v
```

### Run in Headless Mode
Set `HEADLESS = True` in `config/config.py`

### Run with Different Browser
Set `BROWSER = "firefox"` in `config/config.py`

## Project Structure

```
insider-selenium-pom/
├── config/
│   ├── config.py                 # Main configuration
│   └── locators.py              # Web element locators
├── pages/                        # Page Object Model classes
│   ├── base_page.py             # Base page class
│   ├── home_page.py             # Home page
│   ├── careers_page.py          # Careers page
│   ├── qa_jobs_page.py          # QA jobs page
│   └── jobs_lever_page.py       # Lever application page
├── tests/
│   ├── base_test.py             # Base test class
│   └── test_insider.py          # Main test scenarios
├── utils/                        # Utility classes
│   ├── driver_manager.py        # WebDriver management
│   ├── logger_config.py         # Logging configuration
│   └── screenshot_manager.py    # Screenshot management
├── reports/                      # Test reports and screenshots
├── logs/                        # Log files
├── requirements.txt
└── run_tests.py                 # Test runner
```

## Page Object Model

### Architecture Overview

The framework uses Page Object Model (POM) design pattern with the following structure:

#### BasePage Class
Foundation class containing common methods for all pages:
- Element interaction methods (find, click, wait)
- Navigation methods (URL handling, window switching)
- Utility methods (scrolling, hovering)

#### Page-Specific Classes
Each web page has a corresponding class inheriting from BasePage:

- **HomePage** - Landing page operations and navigation
- **CareersPage** - Career page verification and QA job navigation  
- **QAJobsPage** - Job filtering and job detail operations
- **JobsLeverPage** - Job application page validation

#### Usage Example
```python
def test_end_to_end_flow(self):
    # Navigate to home page
    home_page = HomePage(self.driver)
    home_page.go_to_url(Config.BASE_URL)
    
    # Navigate to careers
    careers_page = home_page.navigate_to_careers()
    careers_page.verify_location_block()
    
    # Filter QA jobs
    qa_jobs_page = careers_page.navigate_to_qa_jobs()
    qa_jobs_page.filter_by_location()
```

### Benefits
- **Maintainability** - Changes in UI require updates only in corresponding page classes
- **Reusability** - Common methods shared across all pages
- **Readability** - Test code becomes more business-focused
- **Scalability** - Easy to add new pages by extending BasePage

## Reporting

### HTML Reports
- **Location**: `reports/html/InsiderTestReport_YYYY-MM-DD_HH-MM-SS.html`
- **Content**: Test results, pass/fail status, execution times

### Log Files  
- **Location**: `logs/insider_automation_YYYYMMDD.log`
- **Levels**: DEBUG, INFO, WARNING, ERROR, CRITICAL

### Screenshots
- **Location**: `reports/screenshots/`
- **Format**: `{test_name}_failed_YYYYMMDD_HHMMSS.png`
- **Trigger**: Automatic capture on test failures

## Troubleshooting

### Common Issues

| Issue | Solution |
|-------|----------|
| WebDriver not found | WebDriver Manager handles this automatically |
| Element not found | Increase timeout values in config.py |
| Browser not opening | Check browser installation, try headless mode |
| Tests running slowly | Reduce implicit wait time or use explicit waits |

### Debug Mode
Enable detailed logging by setting log level to DEBUG in `utils/logger_config.py`

## Sample Test Results

```
test_insider.py::TestInsider::test_end_to_end_insider_flow 

============================= 1 passed in 44.89s ==============================
PASSED        [100%]2025-07-31 18:36:30 | INFO | insider_logger | STARTING INSIDER TEST AUTOMATION
2025-07-31 18:36:30 | INFO | insider_logger | Starting WebDriver...
2025-07-31 18:36:38 | INFO | insider_logger | WebDriver started successfully!
2025-07-31 18:36:38 | INFO | insider_logger | Step 1: Home page verification
2025-07-31 18:36:40 | INFO | insider_logger | Accepted cookies...
2025-07-31 18:36:40 | INFO | insider_logger | Looking for cookie popup...
2025-07-31 18:36:41 | INFO | insider_logger | Cookies accepted successfully
2025-07-31 18:36:41 | INFO | insider_logger | Home page verification successful.
2025-07-31 18:36:41 | INFO | insider_logger | Step 2: Careers page verification
2025-07-31 18:36:41 | INFO | insider_logger | Hovering over Company menu...
2025-07-31 18:36:42 | INFO | insider_logger | Waiting for Careers link...
2025-07-31 18:36:46 | INFO | insider_logger | Clicking on Careers link...
2025-07-31 18:36:46 | INFO | insider_logger | Successfully navigated to Careers page
2025-07-31 18:36:46 | INFO | insider_logger | Checking locations block...
2025-07-31 18:36:47 | INFO | insider_logger | Locations block verified successfully
2025-07-31 18:36:47 | INFO | insider_logger | Checking teams block...
2025-07-31 18:36:48 | INFO | insider_logger | Teams block verified successfully
2025-07-31 18:36:48 | INFO | insider_logger | Checking Life at Insider block...
2025-07-31 18:36:49 | INFO | insider_logger | Life at Insider block verified successfully
2025-07-31 18:36:49 | INFO | insider_logger | Careers page verification successful.
2025-07-31 18:36:49 | INFO | insider_logger | Step 3: QA jobs filtering
2025-07-31 18:36:52 | INFO | insider_logger | Clicked 'See all QA jobs' button
2025-07-31 18:36:52 | INFO | insider_logger | Applying location filter...
2025-07-31 18:37:02 | INFO | insider_logger | Department filter loaded: Quality Assurance is visible.
2025-07-31 18:37:02 | INFO | insider_logger | Location dropdown opened
2025-07-31 18:37:03 | INFO | insider_logger | Istanbul, Turkiye selected
2025-07-31 18:37:03 | INFO | insider_logger | Location filter applied successfully
2025-07-31 18:37:03 | INFO | insider_logger | Scrolled to job listings section
2025-07-31 18:37:03 | INFO | insider_logger | QA jobs filtering successful.
2025-07-31 18:37:03 | INFO | insider_logger | Step 4: Job details verification
2025-07-31 18:37:03 | INFO | insider_logger | Verifying job details...
2025-07-31 18:37:08 | INFO | insider_logger | 2 job listings verified successfully
2025-07-31 18:37:08 | INFO | insider_logger | Job details verification successful.
2025-07-31 18:37:08 | INFO | insider_logger | Step 5: Lever redirect and validation
2025-07-31 18:37:08 | INFO | insider_logger | Switched to new Lever tab.
2025-07-31 18:37:11 | INFO | insider_logger | Lever page verification successful.
2025-07-31 18:37:11 | INFO | insider_logger | END-TO-END TEST COMPLETED SUCCESSFULLY!
2025-07-31 18:37:11 | INFO | insider_logger | Closing WebDriver...
2025-07-31 18:37:15 | INFO | insider_logger | WebDriver closed successfully
2025-07-31 18:37:15 | INFO | insider_logger | TEST AUTOMATION COMPLETED - Duration: 44.12 seconds

Process finished with exit code 0

```

## Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/new-feature`)
3. Commit changes (`git commit -am 'Add new feature'`)
4. Push to branch (`git push origin feature/new-feature`)
5. Create Pull Request

## License

This project is licensed under the [MIT License](LICENSE).
