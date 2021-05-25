# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         binary_tree_level_oreder
# Description:  二叉树的层级遍历，每层以数组输出
# Author:       zhaomengyi
# Date:         2021/5/18
# NO:LC102
# 解法：1、使用BFS广度优先搜索，如何判断一层的末节点：两种办法:a.把每层信息加到queue中，空间复杂；
# b.每次进行BFS进行扫描，BatchProcess，这样不需要在queue中加其他信息。
#   2、使用DFS，每次进行深度遍历的时候，对深度进行标记
# 两种方法的时间复杂度都是O(n)
#-------------------------------------------------------------------------------
# Definition for a binary tree node.
import collections
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    #广度优先的解法
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:return []

        result = []
        queue = collections.deque()
        queue.append(root)

        #存储访问结点，如果是图的话
        #visited = set(root)

        #只要队列不为空就弹
        while queue:
            level_size = len(queue)
            current_level = [] #存储当前层的节点

            for _ in range(level_size): #【关键思路】遍历的时候将上一层的元素出队，将下一层的元素入队
                node = queue.popleft() #已有元素出队
                current_level.append(node.val)#当前层加入
                if node.left:queue.append(node.left)#放入下一层几点
                if node.right:queue.append(node.right)

            result.append(current_level)

        return result

    #深度优先，递归解法
    def levelOrder1(self, root: TreeNode) -> List[List[int]]:
        if not root:return []
        self.result = []
        self.dfs(root,0)
        return self.result

    def dfs(self,node,level):
        if not node: return
        if len(self.result) < level+1: #【这里注意】当到达当前层的时候，当前result的集合小于层数，说明这一层的结果集还没添加，在结果中把这一层加上
            self.result.append([])
        self.result[level].append(node.val)

        self.dfs(node.left,level+1)
        self.dfs(node.right,level+1)