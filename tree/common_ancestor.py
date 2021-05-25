# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         common_ancestor
# Description:  判断一棵树两个节点的最近公共祖先，【要理解这个】
# Author:       zhaomengyi
# Date:         2021/5/17
# NO:LC236、235
# 解法：使用递归方法findPorQ，在root结点下root==p or root == q return root，否则的话findPorQ(root.left,p,q)
# findPorQ(root.right,p,q),如果根既不是p也不是q，那么就去左子树和右子树中去找，
#-------------------------------------------------------------------------------
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None or root == p or root == q : return root
        left = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right,p,q)
        if left is None:
            return right
        elif right is None:
            return left
        else:#若果左边和右边都存在p和q说明这个root就是最近的公共父节点
            return root