# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         triangle_short_way
# Description:  三角形图形找出最小的路径
# Author:       zhaomengyi
# Date:         2021/5/20
# NO:LC120
# 解法：方法1递归，traverse(i,j) traverse(i+1,j),traverse(i+1,j+1),时间复杂度O(2^n)
# 方法2：动态规范DP，（1）状态定义，从树的最下层叶子往根推DP[i,j],DP存储当前点回溯的长度大小
# DP :bottom->（i,j）,path sum,min
# （2）DP方程 DP[i,j]=min(DP(i+1,j),DP(i+1,j+1))+Triangle[i,j]
# DP[m-1,]=Triangle[m-1,j]从最深的一层开始
# 时间复杂度O(m*n)
#-------------------------------------------------------------------------------
#用一个一维数组反复使用每次迭代的mini中间结果，这种也叫做状态压缩
from typing import List


class Solution:
  def minimumTotal(self, triangle: List[List[int]]) -> int:
    if not triangle:return 0

    res = triangle[-1] #初始的时候等于最后一行，往上一层逐层回溯
    for i in range(len(triangle)-2,-1,-1):
      for j in range(0,len(triangle[i])):
       res[j] = min(res[j],res[j+1]) + triangle[i][j]
    return res[0]