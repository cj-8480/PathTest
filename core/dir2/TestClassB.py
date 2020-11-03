#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/11/3 9:36
# @Author  : jun.chen
# @Email   : jun.chen_8480@foxmail.com
# @File    : TestClassB.py
# @Software: PyCharm
from core.dir1.TestClassA import ClassA


class ClassB:
    def get_root_path(self):
        classA = ClassA()
        return classA.get_root_path()

    def printMsg(self, msg):
        print("\033[0;36m%s\033[0m" % msg)


if "__main__" == __name__:
    classB = ClassB()
    classB.printMsg("ClassB_Print:\t\t" + classB.get_root_path())
