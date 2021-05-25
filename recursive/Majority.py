# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         Majority
# Description:  找出数组中一个数大于n/2
# Author:       zhaomengyi
# Date:         2021/5/18
# NO:LC169
# 解法：1、开一个Map存储计数 2、排序O(nLogn)
# 3、分治算法，把数组一分为二，左边调majority(),右侧同理，如果left==right，左右两边的majority一致，
# 否则返回最大一侧的元素，时间复杂度O(nlogn)
# 4、使用摩尔投票法可以达到O(n)的时间复杂度和O(1)的空间复杂度，因为有元素肯定大于一半的数量，挨个统计元素，如果相等+1，不相等-1，当小于0时，对下一个投票
#-------------------------------------------------------------------------------
from typing import List


class Solution:
    def recursive(self,nums:List[int],begin:int,end:int):
        if begin == end:
            return nums[begin]
        else:
            mid = int((begin+end)/2)
            left = self.recursive(nums,begin,mid)
            right = self.recursive(nums,mid+1,end)
            #递归结束条件
            if left == right:
                return left
            else:
                cnt_left = 0
                cnt_right = 0
                for i in range(begin,mid):
                    if nums[i] == left:
                        cnt_left = cnt_left+1
                for i in range(mid,end):
                    if nums[i] == right:
                        cnt_right = cnt_right+1
                if cnt_left > cnt_right:
                    return left
                else:
                    return right


    #使用摩尔投票
    def moore(self,nums:List[int])->int:
        cur_ele = 0
        cnt = 0
        for n in nums:
            if cnt == 0:
                cur_ele = n
            if n == cur_ele:
                cnt = cnt+1
            else:
                cnt = cnt-1
        return cur_ele

    def majorityElement(self, nums: List[int]) -> int:
        return self.recursive(nums,0,int(len(nums)-1))



if __name__ == '__main__':
    print(Solution().majorityElement([3,2,3]))