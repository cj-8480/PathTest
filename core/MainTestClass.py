#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/11/3 9:36
# @Author  : jun.chen
# @Email   : jun.chen_8480@foxmail.com
# @File    : MainTestClass.py
# @Software: PyCharm
from PathUtil import PathUtil
from core.dir1.TestClassA import ClassA
from core.dir2.TestClassB import ClassB

# 直接使用工具类
print("-------------------------------")
print("PathUtil:")
print("-------------------------------")
PathUtil.printMsg("init_RootPath:\t\t" + PathUtil.root_path)
print("-------------------------------")
PathUtil.printMsg("func_RootPath:\t\t" + PathUtil.get_root_path())

# ClassA中输出
print("\n")
classA = ClassA()
print("-------------------------------")
print("ClassA:")
print("-------------------------------")
PathUtil.printMsg("init_RootPath:\t\t" + classA.root_path)
PathUtil.printMsg("func_RootPath:\t\t" + classA.get_root_path())

# ClassB中输出
classB = ClassB()
print("-------------------------------")
print("ClassB:")
print("-------------------------------")
PathUtil.printMsg("func_RootPath:\t\t" + classB.get_root_path())
