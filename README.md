从2026.11.18日开始 我将在此记录deepseek每天为我生成的练习的学习过程

在此之前 我已经学习过了几天 现在想用github来记录我的学习之旅

## 2026.11.17学习的内容：坐标计算器

我从中学到的内容是：

1. 在函数中可以传入元组 并且可以对齐进行拆包

```python
def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
```

2. 对于以下这段代码：

```python
while True:
    try:
        quiry = int(input('请输入要查询的年份:'))
        break
    except ValueError:
        print('请输入整数!!!')

found = False
for movie, year in p1:
    if year == quiry:
        print(f"{movie}:{year}")
        found = True
if not found:
    print('没有找到')
```

这里 while True（死循环）的作用是：如果不加这个死循环，那么当用户输入的值不是 int 类型时，try-except 只会执行一次，导致下方的 `if year == quiry` 判断时还是会报错。

因此 while True 可以让用户一直输入，直到输入正确。

其次，我在 `for movie, year in p1` 这段代码也学到了用 found 作为标记。因为如果不标记，就会出现：

```python
for movie, year in p1:
    if year == quiry:
        print(f"{movie}:{year}")
    else:
        print('没有找到电影')
```

由于循环的原因，会导致每次遍历 year 如果都没有，那么 else 语句就会执行好几次。

但是如果用「标记」，那么他就只会执行一次。

## 2026.11.18学习内容:班级名单对比器

我从中学到的内容是:

1. 列表推导式 list = [x for x in list]
2. sorted为内置函数 与list中的sort不同 sorted的用法是这样的 sorted(可迭代对象) 而sort的用法是这样的 list.sort()
3. 自动拆包 *可迭代对象 这里用到的是print(*result) 这里result是升序后的集合 *result可以直接输出其中的内容
4. 集合的内容 set_a - set_b (在a不在b) set_a | set_b (a并b) set_a & set_b (a∩b)
5. 集合可以直接转换为列表 list_1 = list(set) 同理 列表也可以转换为集合 set_1 = set(list)
6. 对比于列表 集合的好处是可以自动去重 可以去重的还有元组


## 2026.11.19学习内容:数字魔法工厂

今天的内容大多都是列表推导式

我从中学到的内容是:

1. 列表推导式可以添加if进行筛选 list = [x for x in list if condition]
2. 列表推导式中的内容可以用函数 list = [int(x) for x in list.split() if condition]


## 2026.11.21学习内容:密码生成器

今天首先在readme文件中学习到了另外两个推导式:

1. 字典推导式 {x : x**2 for x in ...}
2. 集合推导式 {x for x in ...}
3. 在练习一中 我有3个内容几乎一致的for循环 它们可以修改的更加精准
   以第一个for循环为例子
   ```python
   for _ in password:
        if _ in UPPERS:
            have_upper = True
            break
   ```
   这里可以将其改为
   ```python
   any(x in UPPERS for x in password)
   ```
   这样子代码变得更加简洁
   其中它还有个all()函数 判断条件是要所有都符合才可以
5. setdefault()函数
   
   在练习3中
   
   在代码中遇到的问题是这样的
   
   要录入的字典是空字典 原本我认为的键值对创建是这样的 dict[n] = value
   
   但是在这题中对应的值是一个列表 而我录入值的过程是一个循环
   
   这样子就会出现一个问题:当对应的键同时出现2个相对应的值以上时 那么前面的值就会被覆盖
   
   因为ai给我的建议就是使用setdefault()函数
   
   dict.setdefault(key,[]).append(value)
   
   这样子就可以一个值对应一个列表 前面的值就不会被覆盖了
   
   
   
