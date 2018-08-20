import sys
import subprocess
from common.common_fun import *
from multiprocessing import Process
import yaml
from test_run.run_case import start_test_case


def start_appium(report_dir, host, port):
    if not check_port(host, port):
        release_port(port)
    subprocess.Popen('appium', shell=True,
                     stdout=open(report_dir + "appium_" + str(host) + '_' + str(port) + '.log', 'x'),
                     stderr=subprocess.STDOUT)


def close_appium(host, port):
    if not check_port(host, port):
        release_port(port)


# 添加到类似于环境变量中
path = os.getcwd()
sys.path.append(path)

# 日志模块
# CON_LOG = './config/log.conf'
# logging.config.fileConfig(CON_LOG)
# logging = logging.getLogger()


# 创建日志文件目录
now = get_time()
report_dir = os.getcwd() + os.sep + 'reports' + os.sep + now + os.sep
test_dir = './test_case'

if not os.path.exists(report_dir):
    os.mkdir(report_dir)

with open('./config/desired_caps.yaml', 'r', encoding='utf-8') as file:
    data = yaml.load(file)

# 启动appium服务
p = Process(target=start_appium, args=(report_dir, data['ip'], data['port']))
p.start()
p.join()


# 启动测试用例
test_case = Process(target=start_test_case(report_dir, test_dir))
test_case.start()
test_case.join()


# 关闭appium

close_appium(data['ip'], data['port'])

# 启动模拟器


# 打包


#
