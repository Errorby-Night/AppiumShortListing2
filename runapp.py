from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
  
desired_cap = {
    "platformName": "android",
    "appActivity": "com.atg.world.activity.SplashActivity",
    "appWaitDuration": "5000",
    "appExecTimeout": "50000",
    "uiautomator2ServerLaunchTimeout": "50000",
    "uiautomator2ServerInstallTimeout": "50000",
    "appPackage": "com.ATG.World",
    "deviceName": "Pixel 5 API 28",
    "driver": "http://localhost:4723/wd/hub"
}

driver = webdriver.Remote(
    command_executor="http://localhost:4723/wd/hub", 
    desired_capabilities=desired_cap
)

email = driver.find_element_by_id("com.ATG.World:id/email")
time.sleep(2)
email.send_keys("wiz_saurabh@rediffmail.com")
time.sleep(2)
password = driver.find_element_by_id("com.ATG.World:id/password")
time.sleep(2)
password.send_keys("Pass@123")
time.sleep(2)
signin = driver.find_element_by_id("com.ATG.World:id/email_sign_in_button")
time.sleep(2)
signin.click()
time.sleep(2)
print("test_LoginWithRightCredential passed")

driver.find_element_by_id("com.ATF.World:id/btnGotit").click()
driver.implicitly_wait(5)

driver.find_element_by_id("com.ATF.World:id/fab").click()
driver.implicitly_wait(5)

driver.find_element_by_id("com.ATF.World:id/image_fab_clicked").click()
driver.implicitly_wait(5)

driver.find_element_by_id("com.ATF.World:id/image_cell").click()
driver.implicitly_wait(5)

driver.find_element_by_id("com.ATF.World:id/toolbar_post_action").click()
driver.implicitly_wait(5)

driver.find_element_by_id("com.ATF.World:id/caption_edit_text").send_keys("First Post via APPIUM")
driver.implicitly_wait(2)

driver.find_element_by_id("com.ATF.World:id/toolbar_post_action").click()
driver.implicitly_wait(5)

driver.find_element_by_id("com.ATF.World:id/selection_done_btn").click()
time.sleep(3)

driver.back()
time.sleep(2)

driver.find_element_by_id("com.ATF.World:id/homeBottomSheetFragment").click()
driver.implicitly_wait(5)

driver.find_element_by_id("com.ATF.World:id/myPostsLabelTextView").click()
driver.implicitly_wait(5)


print("Done")
driver.quit()
