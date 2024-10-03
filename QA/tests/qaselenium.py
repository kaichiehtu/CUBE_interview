import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@pytest.fixture(scope="module")
def driver():
    # Set up the Chrome driver
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    yield driver
    driver.quit()

def test_screenshot_homepage(driver):
    # Open Cathay United Bank homepage
    driver.get("https://www.cathaybk.com.tw/cathaybk/")
    # Wait for the page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    # Take a screenshot
    driver.save_screenshot("homepage_screenshot.png")
    logging.info("Homepage screenshot taken")

def test_navigate_and_screenshot_credit_cards(driver):
    # Open Cathay United Bank homepage
    driver.get("https://www.cathaybk.com.tw/cathaybk/")
    # Wait and click on the menu
    menu_locator = (By.CSS_SELECTOR, '.menu-toggle')  # Update the selector based on the actual site
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(menu_locator)).click()

    # Navigate to "Credit Cards List"
    personal_finance = (By.LINK_TEXT, "個人金融")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(personal_finance)).click()

    product_intro = (By.LINK_TEXT, "產品介紹")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(product_intro)).click()

    credit_card_list = (By.LINK_TEXT, "信用卡列表")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(credit_card_list)).click()

    # Take a screenshot after navigating
    driver.save_screenshot("credit_cards_list_screenshot.png")
    logging.info("Credit cards list screenshot taken")

    # Count the number of credit card items
    card_items = driver.find_elements(By.CLASS_NAME, "card-item")  # Update selector based on actual site
    num_items = len(card_items)
    logging.info(f"Found {num_items} credit card items")
    assert num_items > 0, "No credit card items found"

def test_count_legacy_credit_cards(driver):
    # Navigate to the credit card description page
    driver.get("https://www.cathaybk.com.tw/cathaybk/credit-card-description")  # Adjust URL as necessary

    # Locate and count legacy cards
    legacy_cards = driver.find_elements(By.XPATH, "//div[contains(text(), '停發')]")  # Adjust path as necessary
    legacy_card_count = len(legacy_cards)
    logging.info(f"Found {legacy_card_count} legacy credit cards")
    assert legacy_card_count > 0, "No legacy cards found"

    # Take a screenshot of the legacy cards section
    driver.save_screenshot("legacy_cards_screenshot.png")

@pytest.mark.usefixtures("driver")
class TestCathayBank:
    def test_screenshots_and_counts(self, driver):
        test_screenshot_homepage(driver)
        test_navigate_and_screenshot_credit_cards(driver)
        test_count_legacy_credit_cards(driver)

if __name__ == "__main__":
    pytest.main()