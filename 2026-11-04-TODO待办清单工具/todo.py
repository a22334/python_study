# ================ 简易待办清单（初学者版） ================
# 这个程序只用到了这些基础知识：
#   变量、列表 list、字典 dict、while 循环、if/elif 判断、
#   input() 输入、print() 输出、函数 def、f-string 格式化
# 运行方法：在该文件夹打开终端，输入  python todo.py  回车

todos = []  # 用一个列表存放所有待办事项，一开始是空的
# 每一条待办是一个字典，例如：{"text": "写作业", "done": False}
# "text" 存待办内容，"done" 存是否完成（True/False）

def show_todos():
    ''''功能1：把所有的待办显示出来'''
    if len(todos) == 0:                 # len() 数一数有几条；0 条就提示
        print("（目前没有待办事项，先添加一条吧）")
        return                          # return 表示这个函数到此结束
    for i in range(len(todos)):         # 循环：i 依次取 0,1,2,...
        t = todos[i]                    # 取出第 i 条待办
        mark = "已完成" if t["done"] else "未完成"   # 根据 done 选显示什么
        print(f"{i + 1}. [{mark}] {t['text']}")     # 编号从 1 开始，方便用户看

def add_todo():
    """功能2：添加一条待办"""
    text = input("请输入待办内容：")    # input() 让用户打字，回车后得到字符串
    todos.append({"text": text, "done": False})   # append 加到列表末尾
    print(f"已添加：{text}")

def done_todo():
    """功能3：把某一条待办标记为已完成"""
    num = int(input("请输入要完成的编号："))   # int() 把字符串转成数字
    index = num - 1                  # 用户看到的是 1 开头，列表下标从 0 开始
    todos[index]["done"] = True      # 修改这条待办的 done 为 True
    print(f"已完成：{todos[index]['text']}")

# ---------- 主循环：程序会一直运行，直到用户选择退出 ----------
while True:                          # 条件永远是 True，所以一直循环
    print()
    print("========== 我的待办清单 ==========")
    show_todos()                     # 先显示当前所有待办
    print()
    print("1. 添加待办")
    print("2. 标记完成")
    print("3. 退出")
    choice = input("请输入数字选择：")

    if choice == "1":                # 字符串和数字比较，注意是 ==
        add_todo()
    elif choice == "2":
        done_todo()
    elif choice == "3":
        print("再见！明天也要加油哦～")
        break                        # break 跳出 while 循环，程序结束
    else:
        print("输入有误，请输入 1、2 或 3")
