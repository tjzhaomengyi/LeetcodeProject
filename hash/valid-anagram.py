# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         valid-anagram
# Description:  判断字符串是否是异位词
# Author:       zhaomengyi
# Date:         2021/5/12
# NO:LC242
# 解法：1、排序O(nlogn) 2、Map存储每个字符，然后判断两个字符串，时间复杂度O(n)
# -------------------------------------------------------------------------------
class Solution:
    def isAnagram(self, s, t):
        dic1, dic2 = {}, {}
        for item in s:
            dic1[item] = dic1.get(item, 0) + 1
        for item in t:
            dic2[item] = dic2.get(item, 0) + 1
        return dic1 == dic2
