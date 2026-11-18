# ================ 学生成绩统计器（11-10 项目，难度 +1） ================
# 新知识点（重点）：
#   1. 字典方法 .items() / .values() —— 遍历字典时拿到"键和值"
#   2. enumerate(列表, 起始编号) —— 遍历时自动编号
# 新知识点（轻量）：
#   sum() / max() / min() 内置函数
# 复习：字典基本操作、in 判断、while 菜单、try/except、文件读写、f-string
# 运行方法：在该文件夹打开终端，输入  python scores.py  回车

scores = {}   # 字典：{"张三": 85.5, "李四": 92}

def add_student():
    """功能1：录入一个学生"""
    name = input("学生姓名：")
    if name in scores:                 # 复习：in 判断名字是否已存在
        print(f"❌ {name} 已经录过了")
        return
    while True:                        # 复习：while + try 输入校验
        try:
            score = float(input("分数："))
            break
        except ValueError:
            print("❌ 请输入数字")
    scores[name] = score               # 复习：字典加/改一个键值对
    print(f"✅ 已录入 {name}：{score} 分")

def show_all():
    """功能2：查看全部学生（今天的主角：items + enumerate）"""
    if not scores:
        print("还没有学生，先录入几个吧")
        return
    for i, (name, score) in enumerate(scores.items(), 1):   # 新知识点：一对对拿出来 + 自动编号
        print(f"{i}. {name}：{score} 分")

def show_stats():
    """功能3：统计平均分 / 最高分 / 最低分"""
    if not scores:
        print("还没有数据")
        return
    values = list(scores.values())     # 新知识点：.values() 把所有分数拿出来（变列表）
    avg = sum(values) / len(values)    # 新知识点：sum() 求和
    print(f"平均分：{avg:.1f}")         # 小技巧：:.1f 保留 1 位小数
    print(f"最高分：{max(values)} 分")   # 新知识点：max() 取最大
    print(f"最低分：{min(values)} 分")   # 新知识点：min() 取最小

def save_to_file():
    """功能4：把成绩保存到文件（复习昨天的文件读写）"""
    with open("成绩.txt", "w", encoding="utf-8") as f:
        for name, score in scores.items():     # 新知识点：items() 遍历
            f.write(f"{name}:{score}\n")
    print("✅ 已保存到 成绩.txt")

# ---------- 主菜单 ----------
while True:
    print()
    print("===== 学生成绩统计器 =====")
    print("1. 录入学生  2. 查看全部  3. 统计  4. 保存到文件  5. 退出")
    choice = input("请选择：")

    if choice == "1":
        add_student()
    elif choice == "2":
        show_all()
    elif choice == "3":
        show_stats()
    elif choice == "4":
        save_to_file()
    elif choice == "5":
        print("再见！")
        break
    else:
        print("❌ 输入有误，请输入 1~5")
