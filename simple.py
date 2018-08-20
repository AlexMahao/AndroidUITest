#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from appium import webdriver
from time import sleep

### 忽略单元测试
from selenium.common.exceptions import NoSuchElementException


class SimpleAndroidTest:
    def __init__(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.4'
        desired_caps['deviceName'] = 'appium3'
        desired_caps['appPackage'] = 'com.souyidai.investment.android'
        # desired_caps['appActivity'] = '.ui.main.MainActivity'
        # 低于5.0不需要权限
        desired_caps['appActivity'] = '.ui.common.LauncherActivity'
        desired_caps['avd'] = 'appium3'
        desired_caps['avdArgs'] = '-gpu host'
        # desired_caps['app'] = '/Users/android-dev/Desktop/appium/HuliClient-debug-3.4.1-PC-resin.apk'
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True
        desired_caps['noReset'] = True;
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)

    def login(self):
        self.logout()
        if self.driver.wait_activity(".ui.passport.LoginActivity", 5):
            self.log_success()
        else:
            self.go_main_activity()
            self.driver.find_element_by_id("com.souyidai.investment.android:id/login").click()
            self.log_success()
        # self.driver.find_element_by_id("com.souyidai.investment.android:id/login").click()
        pass


    def log_success(self):
        self.driver.find_element_by_id('com.souyidai.investment.android:id/user_name').clear()
        self.driver.find_element_by_id("com.souyidai.investment.android:id/user_name").send_keys('13866666666')
        self.driver.find_element_by_id("com.souyidai.investment.android:id/password").send_keys('a1111111')
        self.driver.find_element_by_id("com.souyidai.investment.android:id/login").click()

    def check_ad_dialog(self):

        try:
            closeBtn = self.driver.find_element_by_id('com.souyidai.investment.android:id/close')
        except NoSuchElementException:
            print('no CancelBtn')
        else:
            print("close AdDialog")
            closeBtn.click()

    def is_login(self):
        print("is_login")
        self.go_main_activity()
        test.driver.find_elements_by_class_name("android.support.v7.app.ActionBar$Tab")[2].click()
        return not test.driver.wait_activity(".ui.passport.LoginActivity", 5)

    def logout(self):
        print("logout")
        # 跳转首页
        if self.is_login():
            print("logout: logout !!!")
            self.go_main_activity()
            test.driver.find_elements_by_class_name("android.support.v7.app.ActionBar$Tab")[2].click()
            self.swipe_up()
            self.swipe_up()
            test.driver.find_element_by_id("com.souyidai.investment.android:id/logout").click()
            test.driver.find_element_by_id("android:id/button1").click()

    def go_main_activity(self):
        print("go_main_activity")
        # 跳转首页
        self.check_ad_dialog()
        result = self.driver.wait_activity(".ui.main.MainActivity", 10)
        if not result:
            self.driver.start_activity("com.souyidai.investment.android", ".ui.main.MainActivity")
            self.check_ad_dialog()

    def get_size(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return x, y

    def swipe_up(self):
        l = self.get_size()
        x1 = int(l[0] * 0.5)  # x坐标
        y1 = int(l[1] * 0.85)  # 起始y坐标
        y2 = int(l[1] * 0.1)  # 终点y坐标
        self.driver.swipe(x1, y1, x1, y2)

    def quit(self):
        self.driver.quit()


if __name__ == '__main__':
    test = SimpleAndroidTest()
    test.login()
