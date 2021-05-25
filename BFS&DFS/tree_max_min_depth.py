# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         tree_max_min_depth
# Description:  计算一棵树的最大深度和最小深度
# Author:       zhaomengyi
# Date:         2021/5/18
# NO:LC104\LC111
# 解法：1、DFS，每次向下递进的时候都要记住当前的level，深度一得到叶子结点就是min，然后继续进行遍历
# 2、BFS，用BFS逐层扫，得到max，扫到最后；用BFS只要出现叶子结点就是最小深度min
# 时间复杂度都是：O(n)
# -------------------------------------------------------------------------------
# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class Solution:
  def maxDepth(self, root: TreeNode) -> int:
    if not root: return 0
    return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

  def minDepth(self, root: TreeNode) -> int:
    if root is None: return 0
    left = self.minDepth(root.left)
    right = self.minDepth(root.right)
    # 如果左子树或者右子树的深度位0，那么就把另外一侧的深度+1即可，否则的话表示左右子树都有结点，找到较小的一侧
    if left == 0 or right == 0:
      return left + right + 1
    else:
      return 1 + min(left, right)
