# ================ 班级名单对比器（11-12 项目，难度 +1） ================
# 新知识点（重点）：
#   集合 set —— 自动去重 + 数学运算（交集 & / 并集 | / 差集 -）
# 复习：while、input().strip()、函数、len()、in、f-string、文件读写
# 运行方法：在该文件夹打开终端，输入  python compare.py  回车

def read_names(tip):
    """让用户输入一个班的名单，返回集合（新知识点：集合自动去重）"""
    names = set()            # 新知识点：空集合（注意不是 {}，{} 是空字典！）
    print(tip + "（每行一个名字，输入 end 结束）：")
    while True:
        name = input("> ").strip()          # 复习：strip() 去掉首尾空格
        if name.lower() == "end":
            break
        if name == "":
            continue                        # 复习：跳过空行
        names.add(name)                     # 新知识点：add() 加元素，重复的自动忽略
    return names

def show_result(title, s):
    """打印一个集合的对比结果"""
    print(f"【{title}】共 {len(s)} 人")
    for name in s:                          # 集合也能直接遍历
        print("  ·", name)

def main():
    class_a = read_names("请输入 A 班名单")
    class_b = read_names("请输入 B 班名单")

    print()
    print("========== 对比结果 ==========")
    show_result("两个班都有的同学（交集）", class_a & class_b)      # 新知识点：& 交集
    show_result("两个班总人数（并集）", class_a | class_b)          # 新知识点：| 并集
    show_result("只在 A 班的同学（差集）", class_a - class_b)       # 新知识点：- 差集
    show_result("只在 B 班的同学（差集）", class_b - class_a)

    # 加分项：把结果存进文件（复习文件写入）
    with open("对比结果.txt", "w", encoding="utf-8") as f:
        f.write(f"A班 ∩ B班（交集）：{class_a & class_b}\n")
        f.write(f"A班 ∪ B班（并集）：{class_a | class_b}\n")
        f.write(f"只在A班：{class_a - class_b}\n")
        f.write(f"只在B班：{class_b - class_a}\n")
    print("✅ 结果已保存到 对比结果.txt")

# ---------- 主循环 ----------
while True:
    print()
    main()
    again = input("再对比一组？(y/n)：")
    if again.lower() != "y":
        print("再见！")
        break
