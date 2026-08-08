# # #
# 1. 输入一个整数，判断它是正数、负数还是零。
# 2. 输入年份，判断是否为闰年。规则：能被 400 整除，或能被 4 整除但不能被 100 整除。
num = int(input("请输入一个整数: "))
if num >0 :
    print("正")
elif num < 0:
    print("负")
else:
    print("零")


year = int(input("请输入年份: "))
if year%400 == 0 or year%4 ==0 and year%100!=0 :
    print("是闰年")
else:
    print("不是闰年")