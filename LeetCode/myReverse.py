# 7. 整数反转
# 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
# 假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。
# 请根据这个假设，如果反转后整数溢出那么就返回 0。

def myReverse(x):
    num_range = [-(2 ** 31), (2 ** 31) - 1]

    is_nga = False

    if x < 0:
        x = -x
        is_nga = True
    str_num = str(x)
    length = len(str_num)
    total = 0
    # 溢出 or 没溢出
    for i in range(length):
        total += int(str_num[i]) * (10 ** i)

    if total > num_range[1] or -total < num_range[0]:
        return 0

    if is_nga:
        total = -total

    return total

num = 199

myReverse(num)
