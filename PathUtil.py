#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/11/3 9:29
# @Author  : jun.chen
# @Email   : jun.chen_8480@foxmail.com
# @File    : PathUtil.py
# @Software: PyCharm
import sys
import os


class InitUtil:
    def __init__(self):
        print("Init_PathUtil:")
        self.root_path = self.get_root_path()

    def get_root_path(self):
        current_file_path = os.getcwd()
        project_root_path = None
        print("current_file_path:\t" + current_file_path)
        index = 0
        for path in sys.path:
            print("sys_path%s:\t\t\t" % index + path)
            index += 1
            if current_file_path == path:
                continue

            if current_file_path.__contains__(path):
                project_root_path = path
                break

        if project_root_path is None:
            # 如果未获取到，说明当前路径为根路径
            project_root_path = current_file_path

            # 替换斜杠
            project_root_path = project_root_path.replace("\\", "/")

        return project_root_path

    def printMsg(self, msg):
        print("\033[0;36m%s\033[0m" % msg)


PathUtil = InitUtil()

if "__main__" == __name__:
    PathUtil.printMsg("RootPath_init:\t\t" + PathUtil.root_path)
    print("\n")
    PathUtil.printMsg("RootPath_func:\t\t" + PathUtil.get_root_path())
