#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/11/3 9:36
# @Author  : jun.chen
# @Email   : jun.chen_8480@foxmail.com
# @File    : TestClassA.py
# @Software: PyCharm
from PathUtil import PathUtil


class ClassA:
    def __init__(self):
        print("Init_ClassA:")
        self.root_path = PathUtil.get_root_path()

    def get_root_path(self):
        return PathUtil.get_root_path()

    def printMsg(self, msg):
        print("\033[0;36m%s\033[0m" % msg)


if "__main__" == __name__:
    classA = ClassA()
    classA.printMsg("ClassB_init_Print:\t\t" + classA.get_root_path())
    print("\n")
    classA.printMsg("ClassB_func_Print:\t\t" + classA.get_root_path())
