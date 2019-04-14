# 485. 最大连续1的个数

# 给定一个二进制数组， 计算其中最大连续1的个数。

def findMaxConsecutiveOnes(nums):
    curr_num = 0
    ret_num = 0
    for data in nums:
        if 1 & data:
            curr_num += 1
        else:
            if ret_num < curr_num:
                ret_num = curr_num
            curr_num = 0
    if ret_num < curr_num:
        ret_num = curr_num
    return ret_num

def findMaxConsecutiveOnes1(nums):
    list1 = list()
    print('暂时放一放')
    pass



def main():
    list1 = [1,0,0,1,1,1,0,0]
    # findMaxConsecutiveOnes(list1)
    findMaxConsecutiveOnes1(list1)
if __name__ == '__main__':
    main()