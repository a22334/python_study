# ================ 数字魔法工厂（11-13 项目，难度 +1） ================
# 新知识点（重点）：
#   列表推导式 —— [表达式 for x in 列表] 一行生成新列表
#   带条件的推导式 —— [表达式 for x in 列表 if 条件]
# 复习：input().split()、int()、try/except、列表、函数、sum()、f-string
# 运行方法：在该文件夹打开终端，输入  python magic.py  回车

def get_numbers():
    """输入一串数字，返回整数列表（复习输入校验）"""
    while True:
        text = input("请输入一串数字（用空格隔开）：")
        parts = text.split(" ")      # 复习：按空格切成字符串列表
        nums = []
        ok = True
        for p in parts:
            try:
                nums.append(int(p))          # 复习：转整数
            except ValueError:
                ok = False                   # 有一个不是数字就算失败
        if ok and len(nums) > 0:
            return nums
        print("❌ 输入有误，请只输入数字并用空格隔开")

def main():
    nums = get_numbers()
    print(f"原列表：{nums}")

    # ---------- 今天的主角：列表推导式 ----------
    squares = [x ** 2 for x in nums]                     # 新知识点：基础推导式（每个数取平方）
    doubled = [x * 2 for x in nums]                      # 新知识点：推导式做变换
    evens = [x for x in nums if x % 2 == 0]              # 新知识点：带 if 条件（只留偶数）
    big = [x for x in nums if x > 10]                    # 新知识点：带 if 条件（只留 >10 的）

    # 传统写法对照（后面注释的这 4 行等价于上面的 evens）：
    # evens = []
    # for x in nums:
    #     if x % 2 == 0:
    #         evens.append(x)

    print(f"平方：{squares}")
    print(f"每个数 ×2：{doubled}")
    print(f"其中的偶数：{evens}")
    print(f"大于 10 的数：{big}")
    print(f"总和：{sum(nums)}")

# ---------- 主循环 ----------
while True:
    print()
    main()
    again = input("再玩一组？(y/n)：")
    if again.lower() != "y":
        print("再见！")
        break
