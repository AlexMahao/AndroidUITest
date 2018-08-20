#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from view.commonView import CommonView
from selenium.webdriver.common.by import By
from common.desired_caps import appium_desired


class LoginView(CommonView):
    activity_login = '.ui.passport.LoginActivity'

    id_go_login_btn = (By.ID, 'com.souyidai.investment.android:id/login')
    id_user_name_et = (By.ID, 'com.souyidai.investment.android:id/user_name')
    id_password_et = (By.ID, 'com.souyidai.investment.android:id/password')
    id_login_btn = (By.ID, 'com.souyidai.investment.android:id/login')

    def login_action(self, username, password):
        if self.is_login():
            self.logout()

        if self.wait_activity(self.activity_login, self.timeout):
            self._login_action(username, password)
        else:
            self.go_main_activity()
            self.find_element(*self.id_go_login_btn).click()
            self._login_action(username, password)

    def _login_action(self, username, password):
        user_name_et = self.find_element(*self.id_user_name_et)
        # user_name_et.clear()
        user_name_et.send_keys(username)

        password_et = self.find_element(*self.id_password_et)
        # password_et.clear()
        password_et.send_keys(password)

        self.find_element(*self.id_login_btn).click()


if __name__ == '__main__':
    l = LoginView(appium_desired())
    l.login_action("15811079371", "1234567788")