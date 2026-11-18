# 今日项目（第 4 天）：简易计算器

一个带"防呆"功能的计算器：输入的不是数字、或除以 0，程序**不会崩溃**，而是友好地提示你重新输入。
今天的核心新知识是 **异常处理 try/except**——写"真正能用的程序"必须会的一招。

## 运行方法

在该文件夹打开终端：

```bash
python calculator.py
```

按提示输入两个数字和运算符（`+ - * /`），试试故意输入 `abc` 或者除以 `0`，看看程序怎么应对。

## 新知识点①：异常处理 try / except（重点）

### 没有 try/except 时会发生什么？
```python
float("abc")        # 报错：ValueError，程序直接崩溃
1 / 0               # 报错：ZeroDivisionError，程序直接崩溃
```
一旦出错，程序当场红字报错、停止运行，用户一脸懵。

### 用 try/except 接住错误
```python
try:
    float(input("请输入数字："))   # 先"试着"做
except ValueError:                 # 如果出的是 ValueError 这种错
    print("那不是数字，请重新输入") # 就走这里，程序继续跑
```

- `try` 后面的代码是"试试看"
- `except 错误类型` 后面的代码是"如果出了这种错，就这么办"
- 没出错就正常往下走，except 里的代码不会执行

### 常见错误类型（记住两个就够）
| 错误类型 | 什么时候出现 | 例子 |
| --- | --- | --- |
| `ValueError` | 类型转换失败 | `float("abc")`、`int("哈哈")` |
| `ZeroDivisionError` | 除以 0 | `1 / 0` |

### 经典组合：while + try = 输入校验
```python
while True:
    try:
        return float(input("请输入数字："))   # 输对了，return 直接结束函数
    except ValueError:
        print("输入不对，再来")                # 输错了，循环回去再问一次
```
"直到你输入对为止"——这种写法以后写任何程序都用得上。

## 新知识点②：字符串方法 .lower()（1 行就够）

```python
"Y".lower()   # -> "y"
"YES".lower() # -> "yes"
```
把字母全变小写，这样用户输入 `y` 或 `Y` 都能识别，判断更宽容。

## 复习：已经学过的

- `float()` 把字符串转成小数（`float("3.5")` → 3.5）
- `if / elif / else` 按运算符走不同分支
- `while True` 主循环
- 函数 `def` + `return`（`get_number` 用 return 直接返回结果）
- f-string 输出结果

## 练习（真正的练习在 练习.py，从零写！）

本项目的练习在专门的 **练习.py** 里：3 道题从易到难，只有题目、示例和空函数骨架，**没有答案**，由你独立从零写完：

1. **成绩等级判断**（复习 if/elif + try/except）
2. **猜数字游戏**（完整小程序：random + 循环 + 次数统计）
3. **ATM 取款机**（挑战题：菜单 + 余额校验，加分项是把余额存进文件）

写完直接 `python 练习.py` 运行。README 只留两个热身小改：

1. 给计算器加 `%` 取余运算符（别忘了除数为 0）
2. 加 `**` 幂运算（`2 ** 10` → 1024）

## 小知识

一个 `try` 后面可以跟多个 `except`，接住不同类型的错误：
```python
try:
    ...
except ValueError:
    print("数字不合法")
except ZeroDivisionError:
    print("不能除以 0")
```
以后你还会学到 `else`（没出错才执行）和 `finally`（无论怎样都执行），异常处理家族就齐了。
