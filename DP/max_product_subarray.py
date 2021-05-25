# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         max_product_subarray
# Description:  乘积最大子序列，必须是子序列，必须连续
# Author:       zhaomengyi
# Date:         2021/5/21
# NO:LC152
# 解法:DP,（1）定义DP[i]为从小标为0到i时候的product subarray的最大值，
#（2）DP[i+1]=DP[i]*nums[i+1],这里有个问题，如果nums[i+1]为负数，那么这个最大值就变成了最小值，
#（3）注意（2）中的正负值问题：a.如果DP[i]是正数，那么nums[i+1]也要是正数；
# b.如果DP[i]是负数就要最小值，nums[i+1]是负数
# 使用一个二维数组保存这两种情况DP[i][j],j用0表示max正数，用1表示min负数
#(4)状态转移方程：if nums[i]>0:DP[i,0]=DP[i-1,0]*nums[i] else nums:DP[i,0]=DP[i-1,1]*a[i]
# 同时记录负数的最小值DP[i,1]= if a[i]>=9:DP[i-1,1]*nums[i] else DP[i-1,0]*a[i]
#-------------------------------------------------------------------------------
import functools
from typing import List

#dp的x轴只需要两位0，1;然后使用滚动数组；每次维护更新DP[x][y],每次只需要前一次的结果
@functools.lru_cache(100)
class Solution:
  def maxProduct(self, nums: List[int]) -> int:
    if nums is None: return 0
    dp=[[0 for _ in range(2)] for  _ in range(2)] #开一个二维数组保存前面计算的值
    dp[0][1],dp[0][0],res = nums[0],nums[0],nums[0]

    for i in range(1,len(nums)):
      x,y = i%2,(i-1)%2
      dp[x][0] = max(dp[y][0]*nums[i],dp[y][1]*nums[i],nums[i])
      dp[x][1] = min(dp[y][0]*nums[i],dp[y][1]*nums[i],nums[i])
      res = max(res,dp[x][0])
    return res

if __name__ == '__main__':
    res = Solution().maxProduct([-2,0,-1])
    print(res)