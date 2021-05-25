# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         n_queens
# Description:  使用位运算解决N皇后
# Author:       zhaomengyi
# Date:         2021/5/20
# NO:LC52
#-------------------------------------------------------------------------------
class Solution:
  def totalNQueens(self, n: int) -> int:
    if n<1: return []
    self.count = 0
    self.DFS(n,0,0,0,0)
    return self.count

  def DFS(self,n,row,cols,pie,na):
    #终止条件
    if row >= n:
      self.count += 1
      return

    bits = (~(cols|pie|na)) & ((1<<n)-1)
    while bits:
      p = bits & -bits #取得最低位的1
      self.DFS(n,row+1,cols|p,(pie|p)<<1,(na|p)>>1)
      bits = bits & (bits-1) #去掉最低位的1

if __name__ == '__main__':
    Solution().totalNQueens(n=4)
