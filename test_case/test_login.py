import unittest
from test_case.base_test_case import BaseCase
from view.loginView import LoginView


class TestLogin(BaseCase):

    # @unittest.skip
    def test_login_error(self):
        l = LoginView(self.driver)
        l.login_action("15811079371", '123456')

        self.assertTrue(l.is_login())

    def test_login_success(self):
        l = LoginView(self.driver)
        l.login_action("15811079371", 'q.890704')
        self.assertTrue(l.is_login())
