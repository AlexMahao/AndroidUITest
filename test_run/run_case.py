import sys
import os
import unittest
from common import common_fun
import BSTestRunner
import logging


# def start_test_case(report_dir, test_dir):
#     discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_*')
#     report_name = report_dir + os.sep + 'result_report.html'
#
#     with open(report_name, 'wb') as f:
#         runner = BSTestRunner.BSTestRunner(stream=f, title='Huli', description="狐狸测试报告")
#         logging.info("start run test case")
#         runner.run(discover)




# 添加到类似于环境变量中
path = os.path.dirname(os.getcwd())
sys.path.append(path)

test_dir = '../test_case'
report_dir = '../reports'

discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_*')

now = common_fun.get_time()
report_name = report_dir + os.sep + now + '-test_report.html'

with open(report_name, 'wb') as f:
    runner = BSTestRunner(stream=f, title='Huli', description="狐狸测试报告")
    logging.info("start run test case")
    runner.run(discover)