from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options

options = UiAutomator2Options().load_capabilities({
    "platformName": "Android",
    "deviceName": "emulator-5554",
    "automationName": "UiAutomator2",
    "app": "C:\\Users\\ko\\IdeaProjects\\appium_test_project\\testApk\\ApiDemos-debug.apk"
})

driver = webdriver.Remote(
    command_executor="http://127.0.0.1:4723",
    options=options
)

# Accessibility 클릭
driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Accessibility").click()

# Accessibility Node Querying 클릭
driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Accessibility Node Querying").click()

# 1초 대기
import time
time.sleep(1)

# 뒤로 가기
driver.back()
driver.back()

driver.quit()