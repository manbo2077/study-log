# 1. 使用 `for` 计算 1 到 100 中所有偶数的和。
# 2. 不断要求输入密码；输入 `python` 时输出“正确”并结束，否则提示重试。


### practice part1
# sum = 0
# for i in range(1,100):
#     if i%2 == 0:
#         sum += i
# print(f"1到100中所有偶数的和为: {sum}")

### practice part2
while(True):
    password = input("请输入密码:")
    if password == "python":
        print("正确")
        break
    else:
        print("密码错误，请重试")