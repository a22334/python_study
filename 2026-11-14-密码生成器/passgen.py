# ================ 密码生成器（11-14 项目，难度 +1） ================
# 新知识点（重点）：
#   字典推导式 —— {键: 值 for ...} 一行生成字典
#   集合推导式 —— {表达式 for ...} 一行生成集合（自动去重）
# 复习：random.choice、列表推导式（昨天学的）、"".join()、字典、while 菜单、try/except
# 运行方法：在该文件夹打开终端，输入  python passgen.py  回车

import random

LOWERS = "abcdefghijklmnopqrstuvwxyz"
UPPERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DIGITS = "0123456789"
SYMBOLS = "!@#$%^&*"
ALL = LOWERS + UPPERS + DIGITS + SYMBOLS

current_password = None    # 保存最近生成的密码

def generate_password(length):
    """生成一个随机密码（复习：列表推导式）"""
    chars = [random.choice(ALL) for _ in range(length)]   # 复习：列表推导式
    return "".join(chars)

def analyze_types(password):
    """统计四种字符类型各多少个（循环 + 字典）"""
    counts = {"小写字母": 0, "大写字母": 0, "数字": 0, "符号": 0}
    for ch in password:
        if ch in LOWERS:
            counts["小写字母"] += 1
        elif ch in UPPERS:
            counts["大写字母"] += 1
        elif ch in DIGITS:
            counts["数字"] += 1
        else:
            counts["符号"] += 1
    return counts

def char_table(password):
    """统计每个字符出现次数 —— 新知识点：集合推导式 + 字典推导式"""
    unique = {ch for ch in password}                        # 新知识点：集合推导式（去重）
    table = {ch: password.count(ch) for ch in unique}       # 新知识点：字典推导式
    return table

def dice_demo():
    """掷 10 次骰子，用集合推导式收集点数（自动去重）"""
    rolls = {random.randint(1, 6) for _ in range(10)}       # 新知识点：集合推导式
    return sorted(rolls)

def get_length():
    """输入密码长度（try/except 校验）"""
    while True:
        try:
            n = int(input("请输入密码长度（6~32）："))
            if 6 <= n <= 32:
                return n
            print("❌ 长度要在 6~32 之间")
        except ValueError:
            print("❌ 请输入数字")

# ---------- 主菜单 ----------
while True:
    print()
    print("===== 密码生成器 =====")
    print("1. 生成随机密码")
    print("2. 分析密码字符")
    print("3. 掷骰子去重演示")
    print("4. 退出")
    choice = input("请选择：")

    if choice == "1":
        n = get_length()
        current_password = generate_password(n)
        print(f"🔑 生成的密码：{current_password}")
        print(f"类型统计：{analyze_types(current_password)}")

    elif choice == "2":
        if current_password is None:
            current_password = input("还没有生成过密码，请输入一个来分析：")
        table = char_table(current_password)
        print("每个字符出现次数（字典推导式）：")
        for ch, cnt in table.items():
            print(f"  {ch}: {cnt} 次")
        print(f"一共用了 {len(table)} 种不同字符（集合推导式去重后）")

    elif choice == "3":
        points = dice_demo()
        print(f"掷了 10 次骰子，出现过的点数：{points}（共 {len(points)} 种）")

    elif choice == "4":
        print("再见！记得用强密码哦～")
        break

    else:
        print("❌ 输入有误，请输入 1~4")
