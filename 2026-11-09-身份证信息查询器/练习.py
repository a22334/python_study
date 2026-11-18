# ==============================================
#  练习.py —— 自己动手，从零开始写！
#  主题：字符串切片大作战
#  怎么用：
#   1. 先读题（注释就是题目）
#   2. 想清楚：输入是什么 → 怎么处理 → 输出什么
#   3. 删掉 pass 写代码
#   4. 取消底部对应行的注释，运行：python 练习.py
# ==============================================

# ---------------- 练习 1：回文判断 ----------------
# 写一个函数 is_palindrome(s)：判断字符串正着读和倒着读是否一样
#   是回文 → 返回 True，不是 → 返回 False
# 再用 while 写 practice1()：循环输入字符串，输出"是回文/不是回文"，输入 q 退出
# 提示：倒过来的写法是 s[::-1]（今天学的切片，步长 -1）
# 示例：
#   请输入：上海自来水来自海上
#   是回文
#   请输入：hello
#   不是回文
from ntpath import exists


def is_palindrome(s):
    if s[::-1] == s:
        print('是回文')
    else:
        print('不是回文')
      # ← 删掉 pass，写你的代码

is_palindrome("伤害自来水来自上海")
is_palindrome("hello")


# ---------------- 练习 2：手机号隐藏器 ----------------
# 写 practice2()：输入 11 位手机号，输出中间 4 位被 * 遮住的形式
#   示例：输入 13812345678 → 输出 138****5678
# 要求：
#   1. 长度不是 11 或不是数字 → 提示"手机号格式不对"并重新问
#   2. 用切片取出前 3 位和后 4 位
# 提示：前 3 位 = s[:3]，后 4 位 = s[-4:]
def practice2():
    phone_number = input('请输入您的手机号:')
    if len(phone_number) != 11:
        print('手机号格式不对')
        practice2()
    elif not phone_number.isdigit():
        print('手机号格式不对')
        practice2()
    else:
        print('手机号格式正确')
    the_first_three_digits = phone_number[:3]
    the_last_four_digits = phone_number[-4:]
    return the_first_three_digits + '****' + the_last_four_digits

print(practice2())
    

# ---------------- 练习 3：字符统计器（挑战题） ----------------
# 写 practice3()：输入一句话，统计每个字符出现几次，按出现顺序打印
#   示例：输入 hello → 输出：
#   h: 1
#   e: 1
#   l: 2
#   o: 1
# 要求：
#   1. 用字典存"字符 → 次数"（复习字典！）
#   2. 遍历字符串，每遇到一个字符就 +1（第一次见到就初始化成 1）
#   3. 加分项：忽略空格，只统计字母/数字/标点
def practice3():
    words = input('请输入测试语句:')
    words_list = list(words)
    result = []
    for word in words_list:
        if word not in result:
            result.append(word)

    counts = []
    for number in range(len(result)):
        counts.append(words_list.count(result[number]))

    wordCount_dict = {}
    for number in range(len(result)):
        wordCount_dict[result[number]] = counts[number]

    return wordCount_dict

print(practice3())    



# ---------------- 运行入口 ----------------
# 一次只运行一个练习：把要运行那一行的 # 删掉即可
# practice1()
# practice2()
# practice3()
