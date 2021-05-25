# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         number_of_1
# Description:  统计整数二进制表示中1的个数
# Author:       zhaomengyi
# Date:         2021/5/20
# NO:LC191
# 解法:使用x&x-1的方法去掉最末尾的1，然后统计次数的方法
#-------------------------------------------------------------------------------
class Solution:
  def hammingWeight(self, n: int) -> int:
    res = 0
    while n:
      n = n&(n-1)
      res = res+1
    return res