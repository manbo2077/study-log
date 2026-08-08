# text = "Hello, World!"
# print(text[0:1])
# print(text.upper())



# 1. 输入姓名，去除首尾空格后输出其长度和大写形式。
# 2. 给定 `"apple,banana,pear"`，将其拆分并逐行输出每种水果。
###practice part1
# name = input("请输入姓名:")
# name = name.strip()
# print(f"长度为:{len(name)}, 大写形式为:{name.upper()}")

###practice part2
fruits = "apple,banana,pear"
fruit_list = fruits.split(",")
for fruit in fruit_list:
    print(fruit)