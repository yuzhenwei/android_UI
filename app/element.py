# -*-coding:utf-8-*-
import os
import time
from fractions import Fraction
from appium.webdriver.common.touch_action import TouchAction
from appium import webdriver

class Element(object):
    def findById(self, driver, id):
        print("获取id")
        return driver.find_element_by_id(id)

    def findByName(self, driver, name):
        return driver.find_element_by_android_uiautomator('new UiSelector().text("' + name + '")')

    def findByClass(self, driver, className):
        print("获取class")
        return driver.find_element_by_class_name(className)

    def findByIds(self, driver, id, index):
        return driver.find_elements_by_id(id)[index]

    def findByNames(self, driver, name, index):
        return driver.find_elements_by_android_uiautomator('new UiSelector().text("' + name + '")')[index]

    def findBycClasses(self, driver, className, index):
        return driver.find_elements_by_class_name(className)[index]

    def InsertImg(self, driver, file_name):
         now = time.strftime('%Y-%m-%d-%H-%M', time.localtime(time.time()))
         file_path = os.path.dirname(os.path.dirname(__file__).split('\app')[0] ) + '\data\image\\' + file_name +now+ '.png'
         print(file_path)
         if driver.get_screenshot_as_file(file_path):
            print("截图保留至:{0}".format(file_path))
         else:
             print("截图保留失败")


    def script(self, driver, src):
        return driver.execute_script(src)

    def Tag(self, driver, value):
        """
        :param driver:
        :param value: (x,y,duration)
        :return:
        """

        #获取点击坐标
        if '，' in value:
            value = value.replace('，',',')
        tag_value = eval(value)
        #判断是否存在长按时间
        if len(tag_value) >2:
            duration = tag_value[2]
        else:
            duration = None
        tag_x = tag_value[0]
        tag_y = tag_value[1]
        #分辨率换算
        ratioX = float("%.2f" % (float(1080) / float(320)))
        ratioY = float("%.2f" % (float(1920) / float(760)))
        #换算后的坐标
        start_x = float("%.2f" % (float(tag_x) / ratioX))
        start_y = float("%.2f" % (float(tag_y) / ratioY))

        time.sleep(2)
        action = TouchAction(driver)
        try:
            if duration:
                duration = duration * 1000
                action.long_press(x=start_x, y=start_y, duration=duration).release()
            else:
                # TouchAction(self.driver).press(None, x, y).release().perform()
                action.tap(x=start_x, y=start_y)
            action.perform()
            return True
        except BaseException as e:
            print(e)
            return False

    def Swipe2(self, driver, start_x, start_y, end_x, end_y, duration=200):
        time.sleep(3)
        try:
            driver.swipe(start_x, start_y, end_x, end_y, duration)
            return True
        except BaseException as e:
            print(e)
            return False

    def Swipe(self, driver, direction, value, during=200):
        """
        swipe UP
        :param during:
        :return:
        """
        time.sleep(3)
        window_size = driver.get_window_size()
        width = window_size.get("width")
        height = window_size.get("height")
        if direction == 'down':
            #上
            i = Fraction(1) - Fraction(value)
            try:
                driver.swipe(width / 2, height * 3 / 4, width / 2, height * i.numerator / i.denominator, during)
                return True
            except Exception as e:
                print(e)
                return False
        elif direction == 'up':
            #下
            i = Fraction(value)
            try:
                driver.swipe(width / 2, height / 4, width / 2, height * i.numerator / i.denominator, during)
                return True
            except Exception as e:
                print(e)
                return False
        elif direction == 'right':
            i = Fraction(1, 4) + Fraction(value)
            try:
                driver.swipe(width / 4, height / 2, width * i.numerator / i.denominator, height / 2, during)
                return True
            except Exception as e:
                print(e)
                return False
        elif direction == 'left':
            i = (Fraction(3, 4) - Fraction(value))
            try:
                driver.swipe(width * 3 / 4, height / 2, width * i.numerator / i.denominator, height / 2, during)
                return True
            except Exception as e:
                print(e)
                return False
        else:
            return False


if __name__ == '__main__':
     E = Element()
     dr = driver.Driver()
     E.InsertImg(dr,"name")

