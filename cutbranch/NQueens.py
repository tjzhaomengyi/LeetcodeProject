# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         NQueens
# Description:  N皇后问题，在同行、同列、同撇、同捺方向上不能同时出现皇后
# Author:       zhaomengyi
# Date:         2021/5/18
# NO:LC51
# 解法: 用数组把已经存储的位置记录下来row[i]、col[j]，遍历过的标记为1，
# （1）如何剪枝撇：i+j=c，pie[i+j]=1
# （2）如何剪枝捺：i-j = c pie[i-j] =1
# （3）如何剪枝列：col[j]=1
# 使用DFS来解决
#-------------------------------------------------------------------------------
from typing import List


class Solution:
  def solveNQueens(self, n: int) -> List[List[str]]:
    if n<1: return []
    self.result = []
    self.cols = set();self.pie = set(); self.na = set()
    self.DFS(n,0,[])
    return self._generate_result(n)

  def DFS(self,n,row,cur_state):
    #停止条件
    if row >= n:
      self.result.append(cur_state)
      return

    for col in range(n):
      if col in self.cols or row+col in self.pie or row-col in self.na:
        continue

      #更新标志，把cols、pie和na标注成不能放queens
      self.cols.add(col)
      self.pie.add(row+col)
      self.na.add(row-col)

      #迭代到下一行,这里相当于用一个递归完成一个对row的for循环
      self.DFS(n,row+1,cur_state+[col])

      #清空标注的列
      self.cols.remove(col)
      self.pie.remove(row+col)
      self.na.remove(row-col)

  def _generate_result(self,n):
    board = []
    for res in self.result:
      for i in res:
        board.append("."*i+"Q"+"."*(n-i-1))
    return [board[i:i+n] for i in range(0,len(board),n)]

if __name__ == '__main__':
    Solution().solveNQueens(4)
