# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         coin_change
# Description:  找零钱
# Author:       zhaomengyi
# Date:         2021/5/23
# NO:LC322
# 解法
#-------------------------------------------------------------------------------
from typing import List
import sys


class Solution:
  def coinChange(self, coins: List[int], amount: int) -> int:
    MAX=amount+1
    dp=[MAX for i in range(0,amount+1)]
    dp[0]=0
    #dp[0]=0 #i元钱取得硬币的个数
    for i in range(1,amount+1):
      for j in range(0,len(coins)):
        if coins[j] <= i:
          dp[i] = min(dp[i],dp[i-coins[j]]+1)



    if dp[-1] == MAX:
      return -1
    else:
      return dp[-1]

if __name__ == '__main__':
    print(Solution().coinChange([1,2,5],11))