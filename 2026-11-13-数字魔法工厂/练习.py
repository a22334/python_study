# ==============================================
#  练习.py —— 自己动手，从零开始写！
#  主题：列表推导式大作战
#  怎么用：
#   1. 先读题（注释就是题目）
#   2. 想清楚：输入是什么 → 怎么处理 → 输出什么
#   3. 删掉 pass 写代码
#   4. 取消底部对应行的注释，运行：python 练习.py
# ==============================================

# ---------------- 练习 1：温度转换器 ----------------
# 写 practice1()：
#   1. 输入一串摄氏温度，用空格隔开，例如：0 20 37 100
#   2. 转成数字列表（复习 int()/float() + try/except）
#   3. 用列表推导式转成华氏温度：c * 9/5 + 32
#   4. 保留 1 位小数输出（提示：f"{f:.1f}" 或 round(f, 1)）
# 示例：
#   请输入摄氏温度（空格隔开）：0 20 37 100
#   华氏温度：[32.0, 68.0, 98.6, 212.0]
def practice1():
    while True:
        temper = input('请输入一串摄氏温度(用空格隔开):')
        temper_list = []
        run = True
        try:
            temper_list = [float(x) for x in temper.split()]
        except ValueError:
            run = False
        if not run or len(temper_list) == 0:
            print('输入有误 请输入整数')
        else:
            temperature_list = [x * 9/5 + 32 for x in temper_list]
            for x in temperature_list:
                print(f'{x:.1f}')
            break
        
    
# ---------------- 练习 2：筛选与变换 ----------------
# 写 practice2()：
#   1. 输入一串数字（可正可负），例如：3 -1 4 -1 5 -9
#   2. 用推导式分别生成并输出：
#      a. 所有正数   b. 所有负数   c. 能被 3 整除的数
#      d. 每个数的相反数（3 -> -3，-1 -> 1）
# 示例：
#   请输入数字（空格隔开）：3 -1 4 -1 5 -9
#   正数：[3, 4, 5]
#   负数：[-1, -1, -9]
#   能被 3 整除：[3, -9]
#   相反数：[-3, 1, -4, 1, -5, 9]
def practice2():
    while True:
        number = input('请输入一串数字(可正可负):')
        positice_number = [float(x) for x in number.split() if float(x) > 0]
        negtive_number = [float(x) for x in number.split() if float(x) < 0]
        three_number = [float(x) for x in number.split() if float(x) % 3 == 0]
        opposite_number = [float(x) * -1 for x in number.split()]
        print(positice_number)
        print(negtive_number)
        print(three_number)
        print(opposite_number)
        break

# ---------------- 练习 3：单词长度统计（挑战题） ----------------
# 写 practice3()：
#   1. 输入一句话，例如：python is a great language
#   2. 用 .split(" ") 切成单词列表
#   3. 用推导式得到每个单词的长度列表
#   4. 输出：每个单词 + 长度；最长单词长度（max）；平均长度（sum/len，保留 1 位）
#   5. 加分项：用推导式输出所有长度超过 3 的单词
# 示例：
#   请输入一句话：python is a great language
#   python:6  is:2  a:1  great:5  language:8
#   最长单词长度：8
#   平均长度：4.4
#   超过 3 个字母的单词：['python', 'great', 'language']
def practice3():
    words = input('请输入一句话:')
    words_list = words.split(' ')
    every_word_len = [len(x) for x in words_list]
    for number in range(0,len(words_list)):
        print(words_list[number],every_word_len[number])
    print(max(every_word_len))
    print(f'{sum(every_word_len)/len(every_word_len):.1f}')
    print(f'超过3个字母的单词{[w for w in words_list if len(w) > 3 ]}')
    
        
# ---------------- 运行入口 ----------------
# 一次只运行一个练习：把要运行那一行的 # 删掉即可
practice1()
practice2()
practice3()
