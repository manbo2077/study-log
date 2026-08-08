# name = input("Please input your name:")
# print(f"Hello, {name}!")

# 1. 输入长和宽，输出矩形面积；允许用户输入小数。
# 2. 输入一个总秒数，输出其中有多少整分钟和剩余秒数。
# # # practice part1
# lenth = float(input("input the lenth of rectangle:"))
# width = float(input("input the width of rectangle:"))
# area = lenth * width
# print(f"S:{area}")

# # # practice part2
total_seconds = int(input("输入总秒数："))
minutes = total_seconds // 60
remaining_seconds = total_seconds % 60
print(f"整分钟数: {minutes}, 剩余秒数: {remaining_seconds}")