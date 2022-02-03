import time

from Utilities.scroll_util import ScrollUtil
from Utilities import configReader


def test_searchVillas(appium_driver):
    driver = appium_driver
    time.sleep(4)
    print(configReader.readConfig('locators',"villas_XPATH"))
    driver.find_element_by_xpath(configReader.readConfig('locators',"villas_XPATH")).click()
    driver.find_element_by_xpath(configReader.readConfig('locators',"area_XPATH")).click()
    driver.find_element_by_id("com.goibibo:id/edtSearch").send_keys("Delhi")
    driver.find_element_by_id("com.goibibo:id/lytRegionTopItem").click()
    driver.find_element_by_xpath(configReader.readConfig('locators',"fromDate_XPATH")).click()
    driver.find_element_by_xpath(configReader.readConfig('locators',"toDate_XPATH")).click()
    # driver.find_element_by_xpath(configReader.readConfig('locators',"continue_XPATH")).click()
    # driver.find_element_by_xpath(configReader.readConfig('locators',"viewstays_XPATH")).click()
    # ScrollUtil.scrollToTextByAndroidUIAutomator("Shubham Vilas",driver)

