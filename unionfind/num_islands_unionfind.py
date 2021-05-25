# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         num_islands_unionfind
# Description:
# Author:       zhaomengyi
# Date:         2021/5/24
#-------------------------------------------------------------------------------
from typing import List


class UnionFind:
  dx = [-1,1,0,0]
  dy = [0,0,-1,1]
  def __init__(self,grid):
    m,n=len(grid),len(grid[0])
    self.count = 0
    self.parent = [-1]*(m*n)
    self.rank = [0]*(m*n)
    for i in range(m):
      for j in range(n):
        if grid[i][j] == '1':
          self.parent[i*n+j] = i*n+j #将二维数组转换成一维数组，初始化的时候将自己指向自己
          self.count += 1

  #递归找父节点
  def find(self,i):
    if self.parent[i] != i:
      self.parent[i] = self.find(self.parent[i])
    return self.parent[i]

  def union(self,x,y):
    rootx = self.find(x)
    rooty = self.find(y)
    if rootx != rooty: #如果不下同做uion
      if self.rank[rootx] > self.rank[rooty]:
        self.parent[rooty] = rootx
      elif self.rank[rootx] < self.rank[rooty]:
        self.parent[rootx] = rooty
      else:
        self.parent[rooty] = rootx
        self.rank[rootx] += 1
      self.count -= 1

class Solution:
  def numIslands(self,grid):
    if not grid or not grid[0]:
      return 0

    uf = UnionFind(grid)
    directions = [(0,1),(0,-1),(-1,0),(1,0)]
    m,n = len(grid),len(grid[0])

    for i in range(m):
      for j in range(n):
        if grid[i][j] == '0':
          continue
        for d in directions:
          nr,nc = i+d[0],j+d[1]
          if nr>=0 and nc>=0 and nr<m and nc<n and grid[nr][nc]=='1':
            uf.union(i*n+j,nr*n+nc)
    return uf.count

if __name__ == '__main__':
  grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
  ]
  nums=Solution().numIslands(grid)
  print(nums)