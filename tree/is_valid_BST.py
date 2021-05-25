# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         is_valid_BST
# Description:  判断是否是一棵有效的二叉搜索树
# Author:       zhaomengyi
# Date:         2021/5/13
# NO:LC98
# 解法：全都是O(n)1、中序遍历升序 2、用递归进行判断，需要向外传两个参数min和max，在参数体里面进行左子树递归得到最大值，
#然后再遍历右子树找最小值，然后左子树的最大值小于根节点，右子树的最小值大于根节点，这样递归
#-------------------------------------------------------------------------------
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        #中序列遍历
        # inorder = self.inorder(root)
        # return inorder == list(sorted(set(inorder)))
        #升级中序遍历判断
        self.prev = None
        return self.helper(root)
        #递归
        #return self.isValid(root,None,None)

    #普通中序遍历，中间型数组低效
    def inorder(self,root):
        if root is None:
            return[]
        return self.inorder(root.left) + [root.val] + self.inorder(root.right)
    #进化一下使用中序遍历进行判断，记住前继结点，然后进行比较
    def helper(self,root):
        if root is None:
            return True
        if not self.helper(root.left):
            return False
        if self.prev and self.prev.val >= root.val:
            return False
        self.prev = root
        return self.helper(root.right)
    #递归方法
    def isValid(self,root:TreeNode,min:TreeNode,max:TreeNode)->bool:
        if root == None: return True;
        if min is not None and root.val<=min: return False
        if max is not None and root.val>=max: return False
        return self.isValid(root.left,min,root) and self.isValid(root.right,root,max)