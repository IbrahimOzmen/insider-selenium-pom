# for maintainability, we can separate web objects by page name
from selenium.webdriver.common.by import By


class HomePageLocators:
    LOGO = (By.CSS_SELECTOR, 'a[href="/"]')
    COMPANY_MENU = (By.XPATH, "//a[contains(text(),'Company')]")
    CAREERS_LINK = (By.XPATH, "//a[contains(text(),'Careers')]")
    ACCEPT_COOKIES_BTN = (By.ID, 'wt-cli-accept-all-btn')


class CareersPageLocators:
    LOCATIONS_BLOCK = (By.XPATH, "//h3[contains(@class, 'category-title-media') and contains(text(), 'Our Locations')]")
    TEAMS_BLOCK = (By.XPATH, "//a[contains(@class, 'btn-outline-secondary') and contains(text(), 'See all teams')]")
    LIFE_AT_INSIDER_BLOCK = (By.XPATH, "//h2[contains(@class, 'elementor-heading-title') and contains(text(), 'Life at Insider')]")


class QAJobsPageLocators:
    SEE_ALL_QA_JOBS_BTN = (By.XPATH, "//a[contains(text(),'See all QA jobs')]")
    LOCATION_FILTER = (By.ID, "select2-filter-by-location-container")
    ISTANBUL_OPTION = (By.XPATH, "//li[contains(@class, 'select2-results__option') and text()='Istanbul, Turkiye']")
    JOB_POSITION = (By.CLASS_NAME, "position-title")
    JOB_DEPARTMENT = (By.XPATH, "//span[contains(@class, 'position-department')]")
    DEPARTMENT_VALUE_FOR_JOB_FILTERING = (By.XPATH, '//span[@id="select2-filter-by-department-container"'
                                                    ' and contains(text(), "Quality Assurance")]')

    JOB_LOCATION = (By.XPATH, "//div[contains(@class, 'position-location')]")
    # Explicit and maintainable locator for job positions
    SENIOR_QA_ENGINEER_VIEW_ROLE = (By.XPATH,
                                    "//a[@href='https://jobs.lever.co/useinsider/78ddbec0-16bf-4eab-b5a6-04facb993ddc']")

    QA_ENGINEER_VIEW_ROLE = (By.XPATH,
                             "//a[@href='https://jobs.lever.co/useinsider/0ba4065b-955a-4661-ad4a-f32479f63757']")

class JobsLeverPageLocators:
    APPLY_BUTTON = (By.XPATH, "//div[@class='postings-btn-wrapper']/a[.='Apply for this job']")
