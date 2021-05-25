# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         num_islands
# Description:  岛屿数量
# Author:       zhaomengyi
# Date:         2021/5/24
# NO:LC200
# 解法：1、染色问题 2、使用并查集
#-------------------------------------------------------------------------------
from typing import List


class Solution:
  dx = [-1,1,0,0]
  dy = [0,0,-1,1]
  def numIslands(self, grid: List[List[str]]) -> int:
    #1、使用DFS方式遍历
    if not grid or not grid[0]: return 0
    self.max_x = len(grid)
    self.max_y = len(grid[0])
    self.grid = grid
    self.visited = set()
    return sum([self.floodfill_DFS(i,j) for i in range(self.max_x)for j in range(self.max_y)])

  def floodfill_DFS(self,x,y):
    if not self._is_valid(x,y):
      return 0
    self.visited.add((x,y))
    for k in range(4):
      self.floodfill_DFS(x+self.dx[x],y+self.dy[k])
    return 1

  def _is_valid(self,x,y):
    if x<0 or x>=self.max_x or y<0 or y>=self.max_y:
      return False
    if self.grid[x][y]== '0' or ((x,y) in self.visited):
      return False
    return True

  def floodfill_BFS(self,x,y):
    if not self._is_valid(x,y):
      return
    self.visited.add((x,y))
    queue = collections.deque()
    queue.append((x,y))

    while queue:
      cur_x,cur_y = queue.popleft()
      for i in range(4):
        new_x,new_y = cur_x + d[i],cur_y + dy[i]
        if self._is_valid(new_x,new_y):
          self.visited.add((new_x,new_y))
          queue.append((new_x,new_y))