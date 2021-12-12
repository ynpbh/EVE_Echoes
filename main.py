#!/usr/bin/python3
# -*- coding=utf-8 -*-
# 创建于 2021/11/17 8:36
# 由LseliePan创建

import tkinter

import win32com.client

# 创建大漠对象
dm = win32com.client.Dispatch("dm.dmsoft")

# 创建Tkinter窗口对象
tk = tkinter.Tk()

# 窗口标题
tk.title("EVE Echose AutoScript")
# 窗口大小
tk.geometry("500x320")


def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    print_hi('PyCharm')
    print(dm.ver())
    tk.mainloop()

