# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         longest_increasing_sequence
# Description:  最长上升子序列，可以不连续
# Author:       zhaomengyi
# Date:         2021/5/22
# NO:LC300 【10，9，2，5，3，7，101，18，20】
# 解法：方法1：DP[i]表示从头元素到第i个元素的最长子序列的长度，结果是max(DP[0],DP[1],....DP[n-1])
# for i:0->n-1: DP[i]=max(DP[j])+1,j:0->1且a[j]<a[i]
# 两个循环i:0->n-1;j:0->i-1,时间复杂度O(n^2)
# 方法二：二分法O(NlogN),也是使用两层循环 for i:0->n-1, for j:0->i-1,把第二个j的循环替换成二分查找来加速
# a.维护一个数组LIS,比如10先进来LIS【10】，这时候9进来把10替换的掉LIS【9】，2也比9小替换掉【2】，
# 【2，5】，3进来二分查找替换5【2，3，7，18，20】，如果比最后一个数小就替换掉最后的值。
# 【宗旨就是如果进来的更小那么就更新为更小的，
# 例子[10,11,12,13,1,2,3,4,5]->[10,11,12,13]->[1,11,12,13]->[1,2,12,13]】
# b.每进来一个元素for i:0->n-1插入到LIS c.LIS.size()就是这个i的最大子序列
#-------------------------------------------------------------------------------
from typing import List


class Solution:
  def lengthOfLIS(self, nums: List[int]) -> int:
    if(nums is None or len(nums) == 0): return 0

    res =1
    dp = [1]*len(nums)
    for i in range(len(nums)):
      for j in range(0,i):
        if nums[j] < nums[i]:
          dp[i] = max(dp[i],dp[j]+1)
      res = max(res,dp[i])

    return res
