
from appium import webdriver
import time

def Driver():
    desired_caps = {'platformName': 'Android',
                    'platformVersion': '7.1.2',
                    'deviceName': '59f44f90',  # 设备名字
                    'appPackage': 'com.qlk.ymz',  # app包名
                    'appActivity': 'com.qlk.ymz.activity.LoginActivity' ,
                    'unicodeKeyboard': True,
                    'resetKeyboard': True,
                    'noReset': False,
                    'automationName': 'uiautomator2'
                    }

    dr = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    dr.implicitly_wait(30)

    return dr

if __name__ == '__main__':
    d = Driver()
    time.sleep(2)
    d.quit()
