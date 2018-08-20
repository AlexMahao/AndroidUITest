#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from view.baseView import BaseView
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import logging
from appium import webdriver


class CommonView(BaseView):
    """
       所有业务相关View的父类，封装业务相关的一些共有方法
    """

    id_ad_dialog_close_btn = (By.ID, 'com.souyidai.investment.android:id/close')

    id_logout_btn = (By.ID, 'com.souyidai.investment.android:id/logout')

    id_android_button1 = (By.ID, 'android:id/button1')

    class_name_action_bar_tab = (By.CLASS_NAME, 'android.support.v7.app.ActionBar$Tab')

    activity_main = '.ui.main.MainActivity'

    activity_login = '.ui.passport.LoginActivity'

    app_package = 'com.souyidai.investment.android'

    timeout = 5

    def check_ad_dialog(self):
        logging.info("=================== check_ad_dialog ==============")
        try:
            ad_dialog_close_btn = self.find_element(*self.id_ad_dialog_close_btn)
        except NoSuchElementException:
            logging.info("ad dialog not exist")
        else:
            logging.info("close ad dialog")
            ad_dialog_close_btn.click()

    def go_main_activity(self):
        logging.info("============ go_main_activity ==========")
        # 跳转首页

        self.check_ad_dialog()
        result = self.wait_activity(self.activity_main, self.timeout)
        if not result:
            self.start_activity(self.app_package, self.activity_main)
            self.check_ad_dialog()

    def logout(self):
        logging.info("============ logout ==========")
        # 跳转首页
        if self.is_login():
            self.go_main_activity()
            self.find_elements(*self.class_name_action_bar_tab)[2].click()
            self.swipe_up()
            self.swipe_up()
            self.find_element(*self.id_logout_btn).click()
            self.find_element(*self.id_android_button1).click()

    def is_login(self):
        logging.info("============ is_login ==========")
        self.go_main_activity()
        self.find_elements(*self.class_name_action_bar_tab)[2].click()
        return not self.wait_activity(self.activity_login, self.timeout)
