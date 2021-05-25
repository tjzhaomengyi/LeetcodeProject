# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         power_of_two
# Description:  判断是否是2的底数
# Author:       zhaomengyi
# Date:         2021/5/20
# NO:LC231,LC338
# 解法:LC231判断x不等于0，x&(x-1)==0表示只有一个1
# LC338：找里面有多少个1，如果给n=2，返回[0,1,1]。开一个数组，count[i]=count[i&(i-1)]+1
#-------------------------------------------------------------------------------
class Solution:
  def isPowerOfTwo(self, n: int) -> bool:
    return n>0 and (n & (n-1)) == 0