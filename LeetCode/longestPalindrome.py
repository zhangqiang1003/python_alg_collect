# 5. 找出最长的回文子串

"""
思路：
asdds"""


def longestPalindrome(s):
    str_length = len(s)
    if not s:
        return s
    for i in range(str_length, 1, -1):
        # print(i)
        # if i == 5:
        #     continue
        for j in range(str_length - i + 1):
            # print('------------i------------', i)
            # print(j)
            str1 = s[j:j + i:]
            # print(str1)
            if str1[::-1] == str1:
                return str1
        # break

    return s[0]


def main():
    strs = 'asdfghjkopoiuytrxcvbnmlkjhgfdertyuiolkhfcvbnmkjhgfdgh'
    strs = 'qrwer'
    strs="bbbabbb"

    ret = longestPalindrome(strs)
    print(ret)


if __name__ == '__main__':
    main()
