# ================ 坐标计算器（11-11 项目，难度 +1） ================
# 新知识点（重点）：
#   元组 tuple —— 用 () 打包一组数据，不能修改，可以"拆包"
# 复习：while、if、函数、float + try/except 输入校验、** 幂运算、f-string
# 运行方法：在该文件夹打开终端，输入  python distance.py  回车

def midpoint(p1, p2):
    """计算两点中点，返回一个元组（新知识点：函数可以返回元组）"""
    x1, y1 = p1        # 新知识点：拆包——把一个元组拆成两个变量
    x2, y2 = p2
    return ((x1 + x2) / 2, (y1 + y2) / 2)   # 新知识点：打包成元组返回

def get_number(prompt):
    """输入校验：直到用户输入合法数字（复习 try/except）"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ 请输入数字")

def main():
    print("===== 坐标计算器 =====")
    x1 = get_number("A 点 x：")
    y1 = get_number("A 点 y：")
    x2 = get_number("B 点 x：")
    y2 = get_number("B 点 y：")

    p1 = (x1, y1)      # 新知识点：用 () 打包成元组
    p2 = (x2, y2)

    # 距离公式（勾股定理）：横差² + 纵差² 再开平方（** 0.5 就是开平方）
    d = ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5   # 新知识点：元组按下标取元素

    print(f"A 点：{p1}，B 点：{p2}")
    print(f"两点距离：{d:.2f}")

    mx, my = midpoint(p1, p2)      # 新知识点：函数返回的元组直接拆包
    print(f"中点坐标：({mx:.1f}, {my:.1f})")

# ---------- 主循环 ----------
while True:
    print()
    main()
    again = input("再算一组？(y/n)：")
    if again.lower() != "y":
        print("再见！")
        break
