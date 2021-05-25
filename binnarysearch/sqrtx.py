# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         sqrtx
# Description:  求一个数的平方根
# Author:       zhaomengyi
# Date:         2021/5/19
# NO:LC69
# 解法：二分查找，因为y=x^2是单调递增的，L=0，R=5终止条件fabs(r-l)<e^-9
#-------------------------------------------------------------------------------
class Solution:
  def mySqrt(self, x: int) -> int:
    if x==0 or x == 1:return x
    l=1;r=x;res=0
    while(l<=r):
      m=int((l+r)/2)
      if m==x/m:
        return m
      elif m > x/m:
        r = m-1
      else:
        l = m+1
        res = m
    return res