from appium import webdriver
import time
import data


class Function:
    app = None

    def __init__(self, driver):
        self.driver = driver

    def open(self, driver, path):
        self.app = webdriver.Remote(command_executor=driver, desired_capabilities=path)
        if path == data.robotPath:
            self.app.find_element_by_name(data.robotRecentPrj).click()
            # Waiting for Robot mode change to Auto
            wait = True
            while wait:
                try:
                    text = self.app.find_element_by_name(data.robotAuto).text
                    if text == data.robotAuto:
                        wait = False
                except:
                    wait = True
        return self.app

    def click(self, element):
        self.app.find_element_by_name(element).click()

    def get(self, element):
        time.sleep(1)
        text = self.app.find_element_by_name(element).text
        return text

    def close(self):
        self.app.quit()
