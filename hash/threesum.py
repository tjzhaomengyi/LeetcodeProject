# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         threesum
# Description:  判断nums中是否存在三个元素，使得a+b+c=0，并且三个元素不相等
# Author:       zhaomengyi
# Date:         2021/5/12
# NO:LC15
# 解法：1、暴力O(n^3) 2、c=-(a+b),把数组放在set,O(1)，这样就是a和b在set中进行2次循环O(n^2)
# 3、sortfind:先排序再找，整个数组进行排序O(NlogN),先给定a，b和c分别从前后进行遍历，如果a+b+c>0向左动c，如果
# a+b+c<0,把b向右移动 O（N^2），这个方法不需要方法2的一个多余空间
#【-4，-1，-1，0，1，2】
#  a   b  ->    <- c
#-------------------------------------------------------------------------------
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums)<3:
            return []
        nums.sort()
        res = []
        for i,v in enumerate(nums[:-2]):
            if i>=1 and v==nums[i-1]:
                continue
            d = {}
            for x in nums[i+1:]:
                if x not in d:
                    d[-v-x]=1
                else:
                    if [v,x,-v-x] not in res:
                        res.append([v,x,-v-x])
        return res