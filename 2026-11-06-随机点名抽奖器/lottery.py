# ================ 随机点名抽奖器（第 3 天，难度 +1） ================
# 新知识点（重点）：
#   random 模块 —— random.choice(列表) 随机挑一个、random.sample(列表, n) 随机挑 n 个不重复
# 新知识点（轻量）：
#   字符串方法 join —— "、".join(列表) 把列表连成字符串
# 复习昨天的旧知识：文件读写 open()/with、os.path.exists、while 菜单、函数、列表、f-string
# 运行方法：在该文件夹打开终端，输入  python lottery.py  回车

import os
import random

NAMES_FILE = "names.txt"      # 名单文件：每行一个名字（可以自己新建）
WINNERS_FILE = "winners.txt"  # 中奖记录文件

def load_names():
    """读取名单；如果名单文件不存在，就用内置默认名单"""
    if not os.path.exists(NAMES_FILE):
        return ["张三", "李四", "王五", "赵六", "孙七", "周八", "吴九", "郑十"]
    with open(NAMES_FILE, "r", encoding="utf-8") as f:
        names = []
        for line in f:               # 复习：文件可以直接一行一行遍历
            name = line.strip()      # 去掉每行首尾的空格和换行
            if name != "":           # 跳过空行
                names.append(name)
    return names

def pick_one(names):
    """功能1：随机点 1 个人"""
    winner = random.choice(names)    # 新知识点：从列表里随机挑一个
    print(f"🎉 被抽中的人是：{winner}")
    save_winner(winner)

def pick_many(names):
    """功能2：随机抽 3 个不重复的人"""
    if len(names) < 3:               # 防御：名单不够 3 人时给提示
        print("名单里不足 3 人，没法抽 3 个哦")
        return
    winners = random.sample(names, 3)   # 新知识点：随机挑 3 个，且不重复
    for w in winners:
        print(f"⭐ {w}")
    save_winner("、".join(winners))  # 新知识点（轻量）：把列表连成"张三、李四、王五"

def save_winner(text):
    """把中奖结果追加到 winners.txt（复习昨天的文件追加写入）"""
    with open(WINNERS_FILE, "a", encoding="utf-8") as f:
        f.write(text + "\n")
    print("已记录到 winners.txt")

def show_winners():
    """功能3：查看历史中奖记录"""
    if not os.path.exists(WINNERS_FILE):
        print("还没有中奖记录，先抽一次吧！")
        return
    print("========== 中奖记录 ==========")
    with open(WINNERS_FILE, "r", encoding="utf-8") as f:
        for line in f:
            print(line, end="")      # 复习：end="" 结尾不换行

# ---------- 主循环（和前两天同款菜单套路） ----------
while True:
    print()
    print("========== 随机点名抽奖器 ==========")
    names = load_names()
    print(f"当前名单共 {len(names)} 人")
    print("1. 随机点 1 名")
    print("2. 随机抽 3 名（不重复）")
    print("3. 查看中奖记录")
    print("4. 退出")
    choice = input("请输入数字选择：")

    if choice == "1":
        pick_one(names)
    elif choice == "2":
        pick_many(names)
    elif choice == "3":
        show_winners()
    elif choice == "4":
        print("下次再玩～")
        break
    else:
        print("输入有误，请输入 1~4")
