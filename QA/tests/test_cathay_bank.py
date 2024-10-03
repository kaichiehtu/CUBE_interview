from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest

@pytest.fixture(scope="module")
def driver():
    # 创建和配置 ChromeOptions
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")  # 浏览器启动时最大化

    # 使用正确的 'options' 参数初始化 WebDriver
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    yield driver
    driver.quit()

def test_screenshot_homepage(driver):
    driver.get("https://www.cathaybk.com.tw/cathaybk/")
    driver.save_screenshot("screenshots/homepage_screenshot.png")

def test_navigate_and_screenshot_credit_cards(driver):
    driver.get("https://www.cathaybk.com.tw/cathaybk/")
    driver.save_screenshot("screenshots/credit_cards_list_screenshot.png")

def test_count_legacy_credit_cards(driver):
    driver.get("https://www.cathaybk.com.tw/cathaybk/credit-card-description")
    driver.save_screenshot("screenshots/legacy_cards_screenshot.png")