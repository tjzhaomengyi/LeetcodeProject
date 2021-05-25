# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         generate_parentheses
# Description:  生成括号对，给出n生成2*n的括号对
# Author:       zhaomengyi
# Date:         2021/5/18
# NO:LC22
# 解法：常用面试题
# 1、数学归纳法
# 2、当n=3时候，字符串长度为6，生成2^2n种可能，然后判断是否合法，这样就做了一个完全的搜索,时间复杂度O(2^2n)
# 3、对2进行改进，对2进行剪枝，（1）如果不合法就不递归（比如上来一个右括号）（2）左括号和右括号数量相等，时间复杂度O(2^n)
#-------------------------------------------------------------------------------

#left和right表示左右两边用了多少括号
from typing import List


class Solution:
  def generateParenthesis(self, n: int) -> List[str]:
    self.list = []
    self.gen(0,0,n,"")
    return self.list

  def gen(self,left,right,n,result):
    if left == n and right == n:
      self.list.append(result)
    if left < n:
      self.gen(left+1,right,n,result+"(")
    elif right<n and left>right:
      self.gen(left,right+1,n,result+")")
