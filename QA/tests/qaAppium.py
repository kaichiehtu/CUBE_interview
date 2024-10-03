from appium import webdriver
import time

# 設置 Appium 連接配置
desired_capabilities = {
    "platformName": "Android",
    "platformVersion": "你的Android版本",
    "deviceName": "你的設備名稱",
    "browserName": "Chrome",
}

# 建立 Appium 連接
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities)

# 1. 打開國泰世華銀行官網
driver.get("https://www.cathaybk.com.tw/cathaybk/")
time.sleep(5)  # 等待頁面加載

# 2. 截圖首頁
driver.save_screenshot("screenshot_homepage.png")

# 3. 點擊左上角選單
menu_button = driver.find_element_by_xpath("//android.widget.Button[@content-desc='Menu']")
menu_button.click()
time.sleep(2)

# 4. 進入 個人金融 > 產品介紹 > 信用卡列表
driver.find_element_by_xpath("//android.widget.TextView[@text='個人金融']").click()
driver.find_element_by_xpath("//android.widget.TextView[@text='產品介紹']").click()
driver.find_element_by_xpath("//android.widget.TextView[@text='信用卡列表']").click()
time.sleep(2)

# 5. 計算信用卡項目數量並截圖
credit_cards = driver.find_elements_by_xpath("//android.widget.TextView[contains(@text, '信用卡')]")
print(f"信用卡項目數量: {len(credit_cards)}")
driver.save_screenshot("screenshot_credit_cards.png")

# 6. 進入 卡片介紹
driver.find_element_by_xpath("//android.widget.TextView[@text='信用卡']").click()
driver.find_element_by_xpath("//android.widget.TextView[@text='卡片介紹']").click()
time.sleep(2)

# 7. 計算所有(停發)信用卡數量並截圖
discontinued_cards = driver.find_elements_by_xpath("//android.widget.TextView[@text='停發']")
print(f"停發信用卡數量: {len(discontinued_cards)}")
driver.save_screenshot("screenshot_discontinued_cards.png")

# 關閉 Appium 驅動
driver.quit()
