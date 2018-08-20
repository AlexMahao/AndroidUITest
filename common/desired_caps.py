#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from appium import webdriver
import logging
import logging.config
import yaml
import os
import sys



def appium_desired():



    caps= os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/config/desired_caps.yaml"
    logging.info(caps)
    with open(caps, 'r', encoding='utf-8') as file:
        data = yaml.load(file)

    desired_caps = {}
    desired_caps['platformName'] = data['platformName']
    desired_caps['platformVersion'] = data['platformVersion']
    desired_caps['deviceName'] = data['deviceName']
    desired_caps['appPackage'] = data['appPackage']
    # desired_caps['appActivity'] = '.ui.main.MainActivity'
    # 低于5.0不需要权限
    desired_caps['appActivity'] = data['appActivity']
    desired_caps['avd'] = data['avd']
    desired_caps['avdArgs'] = data['avdArgs']
    # desired_caps['app'] = data['app']
    desired_caps['unicodeKeyboard'] = data['unicodeKeyboard']
    desired_caps['resetKeyboard'] = data['resetKeyboard']
    desired_caps['noReset'] = data['noReset']

    logging.info('start app ...')
    driver = webdriver.Remote('http://' + str(data['ip']) + ':' + str(data['port']) + '/wd/hub', desired_caps)
    driver.implicitly_wait(6)
    return driver


if __name__ == '__main__':
    appium_desired()
