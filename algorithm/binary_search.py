"""
二分法查找-简介

二分法查找，也称为折半法，是一种在有序数组中查找特定元素的搜索算法。

二分法查找的思路如下：

（1）首先，从数组的中间元素开始搜索，如果该元素正好是目标元素，则搜索过程结束，否则执行下一步。

（2）如果目标元素大于/小于中间元素，则在数组大于/小于中间元素的那一半区域查找，然后重复步骤（1）的操作。

（3）如果某一步数组为空，则表示找不到目标元素。

二分法查找的时间复杂度O(logn)。
"""
"""
二分法查找的前提条件：从有序数组[列表]中进行查找
"""

"""
需求：
二分法查找指定数值key在数组（列表）中的索引位置，如果未找到，返回None
"""


# 数组为升序
def binary_search_rise(list1, key):
    low = 0
    height = len(list1) - 1
    while low <= height:
        mid = (low + height) // 2
        if list1[mid] < key:
            # 比目标值小
            low = mid + 1
        elif list1[mid] > key:
            # 比目标值大
            height = mid - 1
        else:
            return mid
    return None


# 数组为降序
def binary_search_drop(list1, key):
    low = 0
    height = len(list1) - 1
    while height >= low:
        mid = (low + height) // 2
        if list1[mid] < key:
            # 比目标值小
            height = mid - 1
        elif list1[mid] > key:
            # 比目标值大
            low = mid + 1
        else:
            return mid
    return None


# list1 = [99, 55, 22, 21, 11, 9, 7, 2]
list1 = [2, 7, 9, 11, 21, 22, 55, 99]
key = 2

# ret = binary_search_drop(list1, key)
ret = binary_search_rise(list1, key)
print(ret)
