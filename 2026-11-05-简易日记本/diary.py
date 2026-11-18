# ================ 简易日记本（第 2 天，难度 +1） ================
# 新知识点（重点）：
#   1. 文件读写 open() / with  —— 把日记保存到文件里，程序关掉数据也不丢
#   2. datetime               —— 自动获取今天的日期时间
# 复习昨天的旧知识：while、if/elif、input/print、函数、f-string、os.path.exists
# 运行方法：在该文件夹打开终端，输入  python diary.py  回车

import os
from datetime import datetime

DIARY_FILE = "diary.txt"   # 日记保存到当前文件夹的 diary.txt 文件里

def write_diary():
    """功能1：写一篇日记（自动带上日期时间）"""
    content = input("今天想记录点什么？")
    if content.strip() == "":            # 复习：strip() 去掉首尾空格
        print("不能写空白日记哦")
        return

    now = datetime.now()                                 # 新知识点①：拿到"当前时刻"
    line = now.strftime("%Y-%m-%d %H:%M") + "  " + content   # 新知识点①：按格式转成字符串

    with open(DIARY_FILE, "a", encoding="utf-8") as f:   # 新知识点②："a" = 追加模式
        f.write(line + "\n")                             # 新知识点②：写入一行
    print("已保存到 diary.txt！")

def read_diary():
    """功能2：把之前写的日记全部读出来"""
    if not os.path.exists(DIARY_FILE):   # 文件还不存在，说明一篇都没写过
        print("还没有写过日记，先写第一篇吧！")
        return

    print("========== 我的日记 ==========")
    with open(DIARY_FILE, "r", encoding="utf-8") as f:   # 新知识点②："r" = 读模式
        lines = f.readlines()                            # 新知识点②：一次读回所有行（列表）

    count = 1
    for line in lines:
        print(f"{count}. {line}", end="")   # end="" 表示结尾不加换行（每行本身已带 \n）
        count = count + 1
    print()

# ---------- 主循环（和昨天的待办清单同款套路） ----------
while True:
    print()
    print("========== 我的日记本 ==========")
    print("1. 写日记")
    print("2. 看日记")
    print("3. 退出")
    choice = input("请输入数字选择：")

    if choice == "1":
        write_diary()
    elif choice == "2":
        read_diary()
    elif choice == "3":
        print("明天也要记录生活哦～")
        break
    else:
        print("输入有误，请输入 1、2 或 3")
