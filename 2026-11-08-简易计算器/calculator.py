# ================ 简易计算器（第 4 天，难度 +1） ================
# 新知识点（重点）：
#   异常处理 try / except —— 程序出错时不崩溃，而是友好地提示
# 新知识点（1 行）：
#   字符串方法 .lower() —— 把字母全变小写
# 复习：while 菜单、if/elif、函数 + return、float() 转数字、f-string
# 运行方法：在该文件夹打开终端，输入  python calculator.py  回车

def get_number(prompt):
    """不断询问，直到用户输入一个合法的数字"""
    while True:
        try:
            return float(input(prompt))   # 新知识点：先"试着"转换数字
        except ValueError:                # 新知识点：转换失败（不是数字）时走这里
            print("❌ 那不是数字，请重新输入")

def calc():
    """做一次运算：读两个数字和一个运算符，输出结果"""
    a = get_number("请输入第一个数字：")
    op = input("请输入运算符（+ - * /）：")
    b = get_number("请输入第二个数字：")

    if op == "+":
        print(f"{a} + {b} = {a + b}")
    elif op == "-":
        print(f"{a} - {b} = {a - b}")
    elif op == "*":
        print(f"{a} × {b} = {a * b}")
    elif op == "/":
        try:                                          # 新知识点：除法可能出错（除以 0）
            print(f"{a} ÷ {b} = {a / b}")
        except ZeroDivisionError:                     # 新知识点：专门接住"除以 0"的错误
            print("❌ 除数不能为 0！")
    else:
        print("❌ 不认识的运算符，请用 + - * /")

# ---------- 主循环：算完一次问要不要再来 ----------
while True:
    print()
    print("========== 简易计算器 ==========")
    calc()
    again = input("再算一次？(y/n)：")
    if again.lower() != "y":    # 新知识点（1行）：.lower() 把 Y/y 都变成小写，方便比较
        print("再见！")
        break
