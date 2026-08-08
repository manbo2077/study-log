# Python 快速上手手写教程

适合对象：有一点 C 基础、刚完成 VS Code 与 `.venv` 配置、希望尽快能读写 Python 程序的人。

这份教程的原则是：**不要只看代码，每段示例都先自己敲一遍、运行一遍，再改一个数字或名称观察结果。**

## 0. 开始前：在项目里运行代码

打开文件夹 `C:\Users\Lenovo\dev\study-log\python`，确认 VS Code 已选择解释器 `.venv\Scripts\python.exe`。每一节可新建一个文件，例如 `01_variable.py`，然后在 VS Code 终端运行：

```powershell
python 01_variable.py
```

Python 用**缩进**表示代码块，通常每层缩进四个空格；不要混用 Tab 和空格。语句通常不需要结尾分号。

---

## 1. 输出、变量与基本类型

### 语法详解

`print()` 向终端输出内容。变量不需要像 C 那样事先声明类型：赋值时名字就绑定到一个对象。

```python
name = "Lin"
age = 20
height = 1.75
is_student = True

print(name)
print(age + 1)
print(type(height))
print(f"{name} 明年 {age + 1} 岁")
```

常见基本类型：`int`（整数）、`float`（小数）、`str`（字符串）、`bool`（布尔值，只有 `True` 和 `False`）、`None`（表示“没有值”）。`f"..."` 是格式化字符串，花括号中可放变量或表达式。

Python 名称惯例使用 `snake_case`，例如 `total_price`。`=` 是赋值，`==` 才是比较是否相等。

### 内存中的本质

C 中变量更接近“固定类型的一块存储位置”。Python 中，整数、字符串、列表等都是**对象**；变量名像贴在对象上的标签。`age = 20` 是让名字 `age` 指向整数对象 `20`。类型属于对象，不属于名字，所以同一个名字之后可以绑定别的类型：`age = "unknown"` 虽然可运行，但通常不建议这样写。

### 手写练习

1. 创建 `city`、`year`、`temperature` 三个变量，输出一句“我在 ___，现在是 ___ 年，温度 ___ 度”。
2. 设 `a = 7`、`b = 3`，分别输出加、减、乘、除和整除的结果。

### 参考答案

```python
# 练习 1
city = "Shanghai"
year = 2026
temperature = 31.5
print(f"我在 {city}，现在是 {year} 年，温度 {temperature} 度")

# 练习 2
a = 7
b = 3
print(a + b, a - b, a * b, a / b, a // b)
```

---

## 2. 运算、输入与类型转换

### 语法详解

算术运算符有 `+ - * / // % **`。其中 `/` 的结果是浮点数，`//` 是向下取整的整除，`%` 是余数，`**` 是乘方。比较运算符为 `== != > >= < <=`，结果是布尔值。逻辑运算使用英文单词：`and`、`or`、`not`。

`input()` 从终端读取一行文本，**返回值永远是字符串**。需要数字时，用 `int()` 或 `float()` 转换。

```python
raw_age = input("请输入年龄：")
age = int(raw_age)

next_age = age + 1
print(f"明年你 {next_age} 岁")
print(10 / 3, 10 // 3, 10 % 3, 2 ** 4)
```

`str()` 可把数字变成文本；`bool()` 会按“是否为空/零”转换真值。初学阶段遇到 `TypeError`，优先检查是否把字符串和数字直接相加了。

### 内存中的本质

大多数数字与字符串对象不可变（immutable）。`score = score + 1` 不是修改旧整数，而是先算出一个新整数对象，再让 `score` 指向它。`input()` 创建一个字符串对象；`int(raw_age)` 则根据其字符内容创建整数对象。

### 手写练习

1. 输入长和宽，输出矩形面积；允许用户输入小数。
2. 输入一个总秒数，输出其中有多少整分钟和剩余秒数。

### 参考答案

```python
# 练习 1
length = float(input("长度："))
width = float(input("宽度："))
print(f"面积：{length * width}")

# 练习 2
seconds = int(input("总秒数："))
minutes = seconds // 60
remaining_seconds = seconds % 60
print(f"{minutes} 分钟 {remaining_seconds} 秒")
```

---

## 3. 条件分支：让程序做选择

### 语法详解

Python 使用 `if`、`elif`、`else`。条件后必须有冒号，后面的代码块必须缩进。和 C 一样，条件表达式会得到真或假；不同的是 Python 也把非空字符串、非空容器、非零数字当作真。

```python
score = int(input("分数："))

if score >= 90:
    level = "A"
elif score >= 60:
    level = "B"
else:
    level = "C"

print(f"等级：{level}")
```

常用写法：`if value is None:` 用于判断是否为 `None`；字符串、数字比较一般用 `==`，不要用 `is`。可写 `if 0 <= score <= 100:`，这是 Python 支持的链式比较。

### 内存中的本质

条件不会“保存一个分支”，而是先计算一个布尔结果，程序根据结果跳到对应的代码块执行。三个分支中只有一个会执行；在分支中赋值的变量，会在当前函数或模块作用域中绑定到相应对象。

### 手写练习

1. 输入一个整数，判断它是正数、负数还是零。
2. 输入年份，判断是否为闰年。规则：能被 400 整除，或能被 4 整除但不能被 100 整除。

### 参考答案

```python
# 练习 1
number = int(input("整数："))
if number > 0:
    print("正数")
elif number < 0:
    print("负数")
else:
    print("零")

# 练习 2
year = int(input("年份："))
is_leap_year = year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)
if is_leap_year:
    print("闰年")
else:
    print("平年")
```

---

## 4. 循环：重复执行

### 语法详解

`for` 最常用来遍历一个序列；`range(start, stop, step)` 生成按规则变化的整数范围，**不包含** `stop`。`while` 在条件为真时持续执行。

```python
total = 0
for number in range(1, 6):
    total += number
print(total)

countdown = 3
while countdown > 0:
    print(countdown)
    countdown -= 1
print("发射")
```

`break` 立刻结束整个循环，`continue` 跳过本轮剩余代码，进入下一轮。循环中的 `else` 存在但较少用：循环未被 `break` 打断时会执行。

### 内存中的本质

`for` 会从可迭代对象依次取元素，让循环变量依次绑定到每个元素对象。`range(1, 6)` 本身不是 C 风格预先塞满 1 到 5 的数组，而是一个能按需产生数字的范围对象。`while` 每次循环前重新计算条件，忘记改变条件变量就会造成死循环。

### 手写练习

1. 使用 `for` 计算 1 到 100 中所有偶数的和。
2. 不断要求输入密码；输入 `python` 时输出“正确”并结束，否则提示重试。

### 参考答案

```python
# 练习 1
total = 0
for number in range(2, 101, 2):
    total += number
print(total)

# 练习 2
while True:
    password = input("密码：")
    if password == "python":
        print("正确")
        break
    print("请重试")
```

---

## 5. 字符串：文本处理

### 语法详解

字符串用单引号或双引号表示。可用下标访问单个字符，索引从 0 开始；负索引从结尾开始。切片 `text[start:stop:step]` 仍然不包含 `stop`。

```python
text = "Python is friendly"
print(text[0])
print(text[-1])
print(text[0:6])
print(text.lower())
print(text.replace("friendly", "powerful"))
```

常用方法：`strip()` 去除两端空白，`split(",")` 按分隔符拆为列表，`"-".join(parts)` 把字符串列表拼接，`len(text)` 得到字符数。方法调用是 `对象.方法()`，例如 `text.upper()`。

### 内存中的本质

字符串是有序、不可变的字符序列。切片、`replace()`、`upper()` 都会返回新的字符串对象，原字符串不改变。这与 C 中你手动操作字符数组不同：Python 自动管理对象内存和字符串结尾，不需要你写 `\0` 或释放内存。

### 手写练习

1. 输入姓名，去除首尾空格后输出其长度和大写形式。
2. 给定 `"apple,banana,pear"`，将其拆分并逐行输出每种水果。

### 参考答案

```python
# 练习 1
name = input("姓名：").strip()
print(len(name))
print(name.upper())

# 练习 2
fruits = "apple,banana,pear".split(",")
for fruit in fruits:
    print(fruit)
```

---

## 6. 列表、元组与字典：组织多个数据

### 语法详解

列表 `list` 用 `[]`，有顺序且可修改；元组 `tuple` 用 `()`，有顺序但不可修改；字典 `dict` 用 `{key: value}`，通过键取值。集合 `set` 用 `{}` 存不重复元素，但初学先掌握前三种即可。

```python
tasks = ["学习", "运动"]
tasks.append("休息")
tasks[0] = "学习 Python"

point = (3, 4)
student = {"name": "Lin", "score": 92}
student["score"] = 95

print(tasks)
print(point[0])
print(student["name"])
```

列表常用 `append()`、`pop()`、`remove()`、`sort()`；字典常用 `get(key, default)`、`keys()`、`values()`、`items()`。遍历字典键和值：`for key, value in student.items():`。

### 内存中的本质

列表是一个可变容器，保存的是对各对象的引用。`a = [1, 2]` 后再写 `b = a`，两个名字指向**同一个列表**；修改 `b` 也会影响 `a`。要复制可写 `b = a.copy()` 或 `b = a[:]`。字典也可变，内部按键快速定位值；键通常必须是不可变对象，如字符串和整数。

### 手写练习

1. 建立一个包含三门课分数的列表，计算平均分，并输出最高分。
2. 建立一个字典保存自己的 `name`、`age`、`city`，用循环逐行输出“键: 值”。

### 参考答案

```python
# 练习 1
scores = [88, 92, 76]
average = sum(scores) / len(scores)
print(f"平均分：{average}")
print(f"最高分：{max(scores)}")

# 练习 2
profile = {"name": "Lin", "age": 20, "city": "Shanghai"}
for key, value in profile.items():
    print(f"{key}: {value}")
```

---

## 7. 函数与作用域：把步骤命名

### 语法详解

用 `def` 定义函数，参数写在括号内，返回值用 `return`。函数体同样依靠缩进。没有写 `return` 的函数默认返回 `None`。

```python
def rectangle_area(length, width):
    """返回矩形面积。"""
    return length * width


area = rectangle_area(3, 4)
print(area)
```

参数可有默认值：`def greet(name, greeting="你好"):`。调用时可以按位置传参，也可以写 `greet(name="Lin")`。变量在函数内赋值后默认是局部变量，函数外同名变量不会因此改变。

### 内存中的本质

定义 `def` 时，Python 创建函数对象，并让函数名指向它；调用时会建立新的调用帧（可理解为一次独立的局部工作区）。参数名在这个局部工作区中绑定到传入的对象。Python 传递的是对象引用：函数修改传入的列表，调用者会看见变化；函数给参数名重新赋值，则只改变局部名字。

### 手写练习

1. 写函数 `is_even(number)`，偶数返回 `True`，否则返回 `False`。
2. 写函数 `add_task(tasks, task)`，将任务加入列表；调用后打印原列表，观察列表是否改变。

### 参考答案

```python
# 练习 1
def is_even(number):
    return number % 2 == 0


print(is_even(8))
print(is_even(7))

# 练习 2
def add_task(tasks, task):
    tasks.append(task)


my_tasks = ["学习"]
add_task(my_tasks, "跑步")
print(my_tasks)
```

---

## 8. 文件与异常：让程序可靠地读写数据

### 语法详解

文件操作推荐使用 `with open(...) as file:`；离开代码块后文件会自动关闭。`"w"` 写入（原内容会被覆盖），`"a"` 追加，`"r"` 读取。指定 `encoding="utf-8"`，中文更稳定。

```python
with open("notes.txt", "w", encoding="utf-8") as file:
    file.write("第一条笔记\n")
    file.write("第二条笔记\n")

with open("notes.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)
```

可能出错的代码用 `try` 包住，并用 `except` 处理预期错误。不要用空的 `except:` 把所有错误悄悄吞掉。

```python
try:
    number = int(input("整数："))
    print(100 / number)
except ValueError:
    print("请输入合法整数")
except ZeroDivisionError:
    print("不能除以零")
```

### 内存中的本质

文件内容不在 Python 进程内存中，而在磁盘上。`open()` 返回文件对象，它记录文件句柄、当前位置和编码等信息；`read()` 才会把数据读入内存并创建字符串对象。异常发生时，Python 沿调用栈寻找匹配的 `except`；`with` 保证无论正常结束还是发生异常，文件都能被关闭。

### 手写练习

1. 让用户输入一句话，追加写入 `diary.txt`，每条占一行。
2. 输入两个整数并输出相除结果；处理“输入不是整数”和“除数为零”两种错误。

### 参考答案

```python
# 练习 1
sentence = input("写一句话：")
with open("diary.txt", "a", encoding="utf-8") as file:
    file.write(sentence + "\n")

# 练习 2
try:
    left = int(input("第一个整数："))
    right = int(input("第二个整数："))
    print(left / right)
except ValueError:
    print("请输入整数")
except ZeroDivisionError:
    print("第二个数不能为零")
```

---

## 9. 模块、包与第三方库

### 语法详解

一个 `.py` 文件就是一个模块。用 `import` 复用模块中的代码：

```python
import math
from datetime import date

print(math.sqrt(9))
print(date.today())
```

你也可以创建 `tools.py`：

```python
def say_hello(name):
    return f"你好，{name}"
```

再在同一文件夹的 `main.py` 中写 `from tools import say_hello`。多个模块放进一个目录（通常有 `__init__.py`）可组成包。

第三方库安装在当前虚拟环境中，例如：

```powershell
python -m pip install requests
python -m pip freeze > requirements.txt
```

使用 `python -m pip` 能确保调用的是当前选中 Python 的 `pip`。不要把文件命名为 `math.py`、`json.py`、`requests.py` 等标准库或已安装库名称，否则会遮蔽真正模块。

### 内存中的本质

首次 `import` 时，Python 会查找模块文件、执行其顶层代码，并创建模块对象；之后通常从 `sys.modules` 缓存中复用，不会每次重新执行。模块名是指向模块对象的引用，`from module import name` 则在当前模块创建一个对该对象的额外绑定。

### 手写练习

1. 创建 `calculator.py`，写 `add(a, b)` 和 `multiply(a, b)`；再创建 `use_calculator.py` 导入并调用它们。
2. 使用 `random` 模块生成 1 到 10 的随机整数，提示用户猜数，并判断是否猜中。

### 参考答案

```python
# calculator.py
def add(a, b):
    return a + b


def multiply(a, b):
    return a * b
```

```python
# use_calculator.py
from calculator import add, multiply

print(add(2, 3))
print(multiply(4, 5))
```

```python
# 随机数练习
import random

answer = random.randint(1, 10)
guess = int(input("猜 1 到 10："))
if guess == answer:
    print("猜中了")
else:
    print(f"没猜中，答案是 {answer}")
```

---

## 10. 面向对象：把数据和行为放在一起

### 语法详解

类是创建对象的模板，用 `class` 定义。`__init__` 是创建对象后自动调用的初始化方法；`self` 表示当前对象，相当于 C++ 成员函数中隐含的 `this`，但 Python 需要把它明确写成第一个参数。

```python
class Task:
    def __init__(self, title, done=False):
        self.title = title
        self.done = done

    def finish(self):
        self.done = True

    def status_text(self):
        return "已完成" if self.done else "未完成"


task = Task("学习 Python")
task.finish()
print(task.title, task.status_text())
```

`self.title` 是对象属性；`task.finish()` 会自动把 `task` 作为 `self` 传入。先用函数和字典能写清楚的程序，没必要强行改成类；当某一类事物有稳定的属性和行为时，类才更合适。

### 内存中的本质

`Task` 是类对象，`Task("学习 Python")` 创建一个实例对象。变量 `task` 指向这个实例；实例内部保存 `title`、`done` 等属性引用。方法本质上也是类上的函数，通过 `task.finish()` 调用时，Python 会把实例自动传入第一个参数 `self`。不同实例各自拥有自己的属性。

### 手写练习

1. 定义 `Counter` 类：初始值为 `0`，有 `increase()` 方法让数值加一，有 `show()` 方法输出数值。
2. 定义 `Book` 类，保存书名和是否借出；写 `borrow()` 方法：未借出时改为借出并返回 `True`，已借出时返回 `False`。

### 参考答案

```python
# 练习 1
class Counter:
    def __init__(self):
        self.value = 0

    def increase(self):
        self.value += 1

    def show(self):
        print(self.value)


counter = Counter()
counter.increase()
counter.show()
```

```python
# 练习 2
class Book:
    def __init__(self, title):
        self.title = title
        self.borrowed = False

    def borrow(self):
        if self.borrowed:
            return False
        self.borrowed = True
        return True


book = Book("Python 入门")
print(book.borrow())
print(book.borrow())
```

---

## 11. 综合练习：命令行待办清单

把前面的知识串起来。请先自己尝试，再看参考实现。目标：循环显示菜单；可以添加任务、查看任务、完成任务、退出。暂时不要求保存到文件。

### 用到的语法

这个小程序会用到列表和字典保存数据、`while True` 保持菜单、`if/elif` 选择功能、函数拆分操作、`enumerate(tasks, start=1)` 取得编号和元素，以及 `try/except` 处理输入错误。

### 内存中的本质

程序运行期间，`tasks` 列表一直存在于内存中，列表中每个字典代表一条任务。函数拿到的是这个列表对象的引用，因此 `append()` 和修改字典中的 `done` 会直接反映到主程序。程序退出后，内存被系统回收，所以任务会消失；下一步可用第 8 节的文件知识把它持久化。

### 手写练习

1. 按目标自己完成待办清单；至少实现“添加”和“查看”。
2. 在程序上增加“删除任务”菜单项：输入任务编号后删除对应任务，并处理无效编号。

### 参考答案

```python
def show_tasks(tasks):
    if not tasks:
        print("暂无任务")
        return
    for index, task in enumerate(tasks, start=1):
        mark = "x" if task["done"] else " "
        print(f"{index}. [{mark}] {task['title']}")


def add_task(tasks):
    title = input("任务内容：").strip()
    if title:
        tasks.append({"title": title, "done": False})


def finish_task(tasks):
    show_tasks(tasks)
    try:
        index = int(input("完成第几项：")) - 1
        tasks[index]["done"] = True
    except (ValueError, IndexError):
        print("编号无效")


tasks = []
while True:
    print("\n1. 添加  2. 查看  3. 完成  0. 退出")
    choice = input("选择：")
    if choice == "1":
        add_task(tasks)
    elif choice == "2":
        show_tasks(tasks)
    elif choice == "3":
        finish_task(tasks)
    elif choice == "0":
        break
    else:
        print("没有这个选项")
```

可自行扩展删除功能。提示：验证编号应在 `0 <= index < len(tasks)` 范围内；删除列表项可用 `tasks.pop(index)`。

---

## 下一步学习路线

完成本教程后，建议顺序如下：

1. 用文件或 JSON 保存第 11 节待办清单。
2. 学习 `venv` 内安装第三方库，尝试 `requests`（网络请求）和 `pytest`（自动测试）。
3. 选择一个方向：自动化脚本、数据分析、Web 后端或爬虫；每次做一个小作品，比连续刷语法更有效。

遇到报错时，先读最下方一行：它通常告诉你错误类型和发生原因；再看它指向的文件与行号。把报错全文、相关代码和你预期的结果保留下来，排查会快得多。
