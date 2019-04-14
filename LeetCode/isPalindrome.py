'''
9 回文数

判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

你能不将整数转为字符串来解决这个问题吗？
'''

def isPalindrome(x):
    if x < 0:
        return False
    elif x < 10 and x >= 0:
        return True
    else:
        list1 = list()
        while True:
            if x // 10:
                list1.append(x % 10)
                x //= 10
            else:
                list1.append(x % 10)
                break

        length = len(list1)
        for i in range(length):
            char = length - i - 1
            if i < char and list1[i] != list1[char]:
                return False
            elif i >= char:
                break
            else:
                continue
        return True


x = 121
ret = isPalindrome(x)
print(ret)