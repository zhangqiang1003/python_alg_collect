'''
10. 正则表达式匹配

给定一个字符串 (s) 和一个字符模式 (p)。实现支持 '.' 和 '*' 的正则表达式匹配。

'.' 匹配任意单个字符。
'*' 匹配零个或多个前面的元素。
匹配应该覆盖整个字符串 (s) ，而不是部分字符串。

说明:

s 可能为空，且只包含从 a-z 的小写字母。
p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。
'''
import time


def isMatch(s, p):
    # 判断p中是否包含.*   .   *
    str_s = s
    reg_1 = '.*'
    reg_2 = '.'
    reg_3 = '*'

    list_1 = p.split(reg_1)
    print(list_1)
    i = 0
    list_2 = list() # 存储被.*筛选出来的字段
    list_3 = list() # 用于存储.筛选出来的字段
    list_4 = list() # 用于存储*筛选出来的字段

    while True:
        # print(list_1[i])
        arr = str_s.split(list_1[i], maxsplit=1)
        # print(arr, 32)
        if arr[0]:
            list_2.append(arr[0])
            if arr[0].find(reg_2) != -1:
                list_3.append(arr[0]) # 筛选出来仅含有.的字段
            if arr[0].find(reg_3) != -1:
                list_4.append(arr[0]) # 筛选出来仅含有*的字段

        if arr[1]:
            str_s = arr[1]
        else:
            break
        i += 1
        # time.sleep(4)

    print(list_2)
    print(list_3)
    print(list_4)




s = 'sdfa.sfs&da.sadassdfadsfasds*sfd'

p = 'sdf.*fs&.*ad.*df.*fasd.*fd'


# p = 'sdfasfs&dasad.*dfadsfasdssfd'
isMatch(s, p)
