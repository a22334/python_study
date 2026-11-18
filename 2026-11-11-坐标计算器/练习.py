# ==============================================
#  练习.py —— 自己动手，从零开始写！
#  主题：元组大作战
#  怎么用：
#   1. 先读题（注释就是题目）
#   2. 想清楚：输入是什么 → 怎么处理 → 输出什么
#   3. 删掉 pass 写代码
#   4. 取消底部对应行的注释，运行：python 练习.py
# ==============================================

# ---------------- 练习 1：三角形周长 ----------------
# 写 distance(p1, p2) 和 practice1()：
#   1. 输入三个点的坐标（共 6 个数），每两个数打包成一个元组
#   2. distance(p1, p2) 计算两点距离：
#      公式 ((x1-x2)**2 + (y1-y2)**2) ** 0.5
#   3. 周长 = 三条边的和，保留 2 位小数输出
# 示例：
#   请输入 A 点 x：0
#   请输入 A 点 y：0
#   请输入 B 点 x：3
#   请输入 B 点 y：0
#   请输入 C 点 x：0
#   请输入 C 点 y：4
#   三角形周长：12.00
def distance(p1, p2):
    x1,y1 = p1
    x2,y2 = p2
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2 ) ** 0.5
   
def practice1(prompt):
    try:
        return float(input(f'请输入{prompt}:'))
    except ValueError:
        print('请输入数字')
    
def main():
    x1 = practice1('A点x')
    y1 = practice1('A点y')
    x2 = practice1('B点x')
    y2 = practice1('B点y')
    x3 = practice1('C点x')
    y3 = practice1('C点y')
    p1 = (x1,y1)
    p2 = (x2,y2)
    p3 = (x3,y3)
    border = distance(p1,p2) + distance(p2,p3) + distance(p1,p3)
    print(f'三角形的周长是{border:.2f}')
# ---------------- 练习 2：交换两个变量 ----------------
# 写 practice2()：输入两个数 a、b，交换后输出
#   提示：x, y = y, x 一行就能交换（元组拆包！）
# 示例：
#   请输入 a：5
#   请输入 b：9
#   交换后：a = 9, b = 5
def practice2():
    a = int(input('请输入a的整数值:'))
    b = int(input('请输入b的整数值:'))
    a , b = b , a
    print(f'a:{a},b:{b}')
# ---------------- 练习 3：迷你电影库（挑战题） ----------------
# 写 practice3()：电影列表，每个元素是一个元组 (片名, 年份)：

movies = [("流浪地球", 2019), ("哪吒之魔童降世", 2019), ("满江红", 2023)]

#   菜单循环：
#     1 查看全部（for title, year in movies 拆包打印）
#     2 按年份查找（输入年份，打印所有那一年的电影；没有则提示"没有找到"）
#     3 退出
#   加分项：4 添加电影（输入片名 + 年份，追加到列表）


# ---------------- 运行入口 ----------------
# 一次只运行一个练习：把要运行那一行的 # 删掉即可
# practice1()
# practice2()
# practice3()

def quiry(p1):
    for movie,year in p1:
        print(f'{year},{movie}')

def quiry_year(p1):
    while True:
        try:
            quiry = int(input('请输入要查询的年份:'))
            break
        except ValueError:
            print('请输入整数!!!')
    found = False
    for movie,year in p1:
        if year == quiry:
            print(f"{movie}:{year}")
            found = True
    if not found:
        print('没有找到')


def add_movie(movie,year):
    new_movie = (movie,year)
    movies.append(new_movie)

while True:
    print()
    print('菜单')
    print('----------------------')
    print('输入1 查看全部')
    print('输入2 按年份查找')
    print('输入3 添加电影')
    print('输入4 退出')
    print('----------------------')
    choice = int(input('请输入:'))
    match choice:
        case 1:
            quiry(movies)
        case 2:
            quiry_year(movies)
        case 3:
            movie = input('请输入要添加的电影名称:')
            while True:
                try:
                    year = int(input('请输入要添加的电影年份:'))
                    break
                except ValueError:
                    print('请输入整数!!!')
            add_movie(movie,year)
        case _:
            break

