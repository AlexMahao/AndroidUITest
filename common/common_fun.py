#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import socket
import os


def get_time():
    return time.strftime("%Y-%m-%d:%H_%M_%S")


def check_port(host, port):
    """检测指定的端口是否被占用"""

    # 创建socket对象
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((host, port))
        s.shutdown(2)
    except OSError as msg:
        print('port %s is available! ' % port)
        print(msg)
        return True
    else:
        print('port %s already be in use !' % port)
        return False


def release_port(port):
    """释放指定的端口"""
    # 查找对应端口的pid
    cmd_find = 'kill -9 $(lsof -i:%s -t)' % port
    # 返回命令执行后的结果
    result = os.popen(cmd_find).read()
    print(result)
