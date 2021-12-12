#!/usr/bin/python3
# -*- coding=utf-8 -*-
# 创建于 2021/11/17 8:36
# 由LseliePan创建

import tkinter

import win32com.client

dm = win32com.client.Dispatch("dm.dmsoft")
tk = tkinter.Tk()

tk.title("EVE Echose AutoScript")
tk.geometry("500x320")


def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    print_hi('PyCharm')
    print(dm.ver())
    tk.mainloop()
# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
