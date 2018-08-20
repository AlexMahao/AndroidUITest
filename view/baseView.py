#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from appium import webdriver


class BaseView(object):
    """ 所有View的基类，封装一些调用appium的方法，便于后期的维护和迭代，
        不包含任何业务相关的逻辑
    """

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, *loc):
        return self.driver.find_element(*loc)

    def find_elements(self, *loc):
        return self.driver.find_elements(*loc)

    def get_window_size(self):
        return self.driver.get_window_size()

    def swipe(self, start_x, start_y, end_x, end_y, duration):
        return self.driver.swipe(start_x, start_y, end_x, end_y, duration)

    def wait_activity(self, activity_name, timeout):
        return self.driver.wait_activity(activity_name, timeout)

    def start_activity(self, app_package, activity):
        return self.driver.start_activity(app_package, activity)

    def get_size(self):
        x = self.get_window_size()['width']
        y = self.get_window_size()['height']
        return x, y

    def swipe_left(self):
        l = self.get_size()
        x1 = int(l[0] * 0.9)
        y1 = int(l[1] * 0.5)
        x2 = int(l[0] * 0.1)
        self.swipe(x1, y1, x2, y1, 10000)

    def swipe_up(self):
        l = self.get_size()
        x1 = int(l[0] * 0.5)
        y1 = int(l[1] * 0.9)
        y2 = int(l[1] * 0.1)
        self.driver.swipe(x1, y1, x1, y2)



