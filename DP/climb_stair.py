# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         climb_stair
# Description:  每次只能爬一个台阶或两个台阶，爬楼梯有多少种方法
# Author:       zhaomengyi
# Date:         2021/5/20
# NO:LC70
# 解法：楼梯和格子走法的问题
# 方法1：递归：f(n)=f(n-1)+f(n-2)表示第n阶台阶的走法就是前一阶台阶的走法和前两阶台阶的走法，这就是一个斐波那契数列的动态规范方法
# 方法2：DP=recursion+memory,for i=2=>n:f[n]=f[n-1]+f[n-2]，时间复杂度O(n)
#-------------------------------------------------------------------------------
import functools


class Solution:
  @functools.lru_cache(100)
  # def climbStairs(self, n: int) -> int:
  #   #   #方法一：
  #   #   if n<=1 :return 1
  #   #   return self.climbStairs(n-1)+self.climbStairs(n-2)
  def climbStairs(self, n: int) -> int:
    if n<=2:return n
    mem = [0] * n
    mem[0]=1
    mem[1]=2
    for i in range(2,n):
      mem[i] = mem[i-1]+mem[i-2]
    return mem[n-1]