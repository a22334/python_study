# ================ 身份证信息查询器（11-09 项目，难度 +1） ================
# 新知识点（重点）：
#   字符串切片 s[start:end] —— 从字符串里"切"一段出来
# 新知识点（1 行）：
#   字符串方法 .isdigit() —— 判断是不是全是数字
# 复习：while、if、len()、int()、% 取余、.lower()、continue、f-string
# 运行方法：在该文件夹打开终端，输入  python idcard.py  回车
#
# 身份证号（18 位）结构：
#   前 6 位 = 地区代码；第 7~14 位 = 出生日期(YYYYMMDD)；
#   第 15~17 位 = 顺序码，其中第 17 位（倒数第 2 位）奇数=男、偶数=女；
#   第 18 位 = 校验码（数字或 X）

def is_valid_id(s):
    """检查身份证号格式是否合法"""
    if len(s) != 18:                          # 长度必须是 18
        return False
    if not s[:17].isdigit():                  # 新知识点：前 17 位必须全是数字
        return False
    if not (s[17].isdigit() or s[17] in "xX"):# 最后一位是数字或 x/X
        return False
    return True

def analyze_id(s):
    """从身份证号里提取信息（今天的主角：切片）"""
    year = s[6:10]      # 新知识点：切下标 6~9（第 7~10 位）
    month = s[10:12]    # 新知识点：第 11~12 位
    day = s[12:14]      # 新知识点：第 13~14 位
    area = s[0:6]       # 新知识点：前 6 位
    gender = "男" if int(s[16]) % 2 == 1 else "女"   # 第 17 位（下标16）决定性别

    print(f"出生日期：{year} 年 {month} 月 {day} 日")
    print(f"性别：{gender}")
    print(f"地区代码：{area}")

# ---------- 主循环 ----------
while True:
    print()
    id_str = input("请输入 18 位身份证号（输入 q 退出）：")
    if id_str.lower() == "q":           # 复习：.lower() 让大小写都能退出
        print("再见！")
        break
    if not is_valid_id(id_str):
        print("❌ 格式不正确：需要 18 位，前 17 位数字，最后一位数字或 X")
        continue                        # 复习：continue = 跳过本次，回到 while 开头
    analyze_id(id_str)
