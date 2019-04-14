# 1. 两数之和

"""
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，
并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
"""


# def two_sum(nums, target):
#     # 判断奇偶性
#     for data in nums:
#         try:
#             ret_a = nums.index(data)
#             ret_b = nums.index(target - data, ret_a + 1)
#         except:
#             pass
#         else:
#             return [ret_a, ret_b]
#
#
# ret = two_sum([50000000, 3, 2, 4, 50000000], 100000000)
# print(ret)

# def two_sum(nums, target):
#     length = len(nums)
#     for i in range(length):
#         num = target - nums[i]
#         if (i + 1) < length and num in nums[i + 1::]:
#             index = nums.index(num, i+1)
#             return [i, index]



# def two_sum(nums, target):
#     ret_num = None
#     first_key = None
#     find_comm = False
#     for key, value in enumerate(nums):
#         num = target - value
#         if ret_num == value:
#             return [first_key, key]
#         elif num == value:
#             if num in nums[key+1::]:
#                 find_comm = True
#                 first_key = key
#                 ret_num = num
#                 continue
#         elif num in nums and not find_comm:
#                 first_key = key
#                 ret_num = num
#                 continue


def two_sum(nums, target):
    temp = {}
    for i in range(len(nums)):
        num = nums[i]
        diff = target - num
        try:
            return [temp[diff], i]
        except:
            temp[num] = i

# ret = two_sum([50000000, 7, 2, 4, 50000000], 100000000)
# ret = two_sum([50, 3, 2, 4], 5)
# ret = two_sum([2,7,11,15], 9)
ret = two_sum([3,2, 4], 6)

# [2,7,11,15]
# 9
print(ret)
