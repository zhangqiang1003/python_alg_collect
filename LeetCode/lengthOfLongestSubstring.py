# 3. 无重复字符的最长子串
# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

def lengthOfLongestSubstring(s):
    if s == '':
        return 0

    str_child = s[0]
    max_len = len(str_child)
    for i in range(1, len(s)):
        if s[i] in str_child:
            if max_len <= len(str_child):
                max_len = len(str_child)
            index = str_child.index(s[i])
            str_child = str_child[index::]
            str_child += s[i]
            str_child = str_child[1::]
            continue
        else:
            str_child += s[i]

        if max_len <= len(str_child):
            max_len = len(str_child)

    return max_len

def lengthOfLongestSubstring1(s):
    if s == '':
        return 0

    str_child = s[0]
    max_len = len(str_child)
    for i in range(1, len(s)):
        if s[i] in str_child:
            if max_len <= len(str_child):
                max_len = len(str_child)
            index = str_child.index(s[i])
            if index < i:
                index = i
            if len(s) > index + 1 + max_len:
                str_child = s[index + 1: index + 1 + max_len:]
                print(str_child)
            else:
                return max_len
            # continue
        else:
            str_child += s[i]

        if max_len <= len(str_child):
            max_len = len(str_child)

    return max_len

def main():
    strs = 'kidnaodoaneosalkfoiek'
    # strs = ' a '
    # strs = 'au'
    # ret = lengthOfLongestSubstring(strs)
    ret = lengthOfLongestSubstring1(strs)
    print(ret)

if __name__ == '__main__':
    main()