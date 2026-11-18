# ==============================================
#  练习.py —— 自己动手，从零开始写！
#  主题：字典大作战（items / enumerate）
#  怎么用：
#   1. 先读题（注释就是题目）
#   2. 想清楚：输入是什么 → 怎么处理 → 输出什么
#   3. 删掉 pass 写代码
#   4. 取消底部对应行的注释，运行：python 练习.py
# ==============================================

# ---------------- 练习 1：英语小词典 ----------------
# 写 practice1()：
#   1. 建一个字典，先存 3 个单词：
#      {"apple": "苹果", "book": "书", "python": "蟒蛇"}
#   2. 循环让用户输入英文单词，输出中文意思；查不到 → "词典里没有这个词"
#   3. 输入 q 退出
# 示例：
#   请输入英文单词：apple
#   苹果
#   请输入英文单词：dog
#   词典里没有这个词
def practice1():
    test_dict = {'apple':'苹果','book':'书','python':'蟒蛇'}
    circuit = True
    word_dict = test_dict.keys()
    chinese_dict = test_dict.values()
    while circuit:
        word = input("请输入要查找的单词('按q退出'):")
        if word == 'q':
            circuit = False
        elif word not in word_dict:
            print('词典里没有这个词')
        else:
            print(test_dict[word])
        

# ---------------- 练习 2：通讯录 ----------------
# 写 practice2()：一个迷你通讯录，菜单循环：
#   1 添加联系人（姓名 + 电话；姓名重复要提示"已存在"）
#   2 查看全部（用 items() + enumerate 编号显示）
#   3 删除联系人（del 字典[姓名]，不存在要提示）
#   4 退出
# 提示：电话用字符串存就行（"13812345678"），不用转数字
def practice2():
    contact_dict = {}
    contact = []
    phone_number = []
    person = input('请输入要添加的联系人:')
    number = input('请输入对应联系人的电话号码')
    if person in contact:
        print('已存在')
    else:
        contact.append(person)
        phone_number.append(number)
    for i in range(len(contact)):
        contact_dict[contact[i]] = phone_number[i]
    

# ---------------- 练习 3：投票统计器（挑战题） ----------------
# 写 practice3()：统计每个人得了多少票
#   1. 循环让用户输入"投票给谁"（每行一个名字），输入 end 结束
#   2. 用字典统计每个名字出现次数（复习：第一次见到初始化为 1，之后 +1）
#   3. 结束后用 items() 打印每个人和票数
#   4. 加分项：排出名次（从票数多到少输出。
#      提示：每次找出票数最多的打印，再把他从字典里删掉，重复直到空；或查一下 sorted()）
# 示例：
#   投票给谁：张三
#   投票给谁：李四
#   投票给谁：张三
#   投票给谁：end
#   张三：2 票
#   李四：1 票
def practice3():
    circuit = True
    candidates = []
    voter = []
    ticket = []
    finaly_dict = {}
    while circuit:
        candidate = input("投票给谁('输入end结束'):")
        if candidate == '':
            print('不能为空')
        elif candidate == 'end':
            circuit = False
        else:
            candidates.append(candidate)
    for person in range(len(candidates)):
        if candidates[person] in voter:
            continue
        else:
            voter.append(candidates[person])       
    for person in range(len(voter)):
        vote = candidates.count(voter[person])
        ticket.append(vote)
    for i in range(len(voter)):
        finaly_dict[voter[i]] = ticket[i]

    sort = finaly_dict.items()
    return sort
# ---------------- 运行入口 ----------------
# 一次只运行一个练习：把要运行那一行的 # 删掉即可
# practice1()
# practice2()
# practice3()
