# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         swap_nodes_in_pairs
# Description:  交换链表中相邻两个节点
# Author:       zhaomengyi
# Date:         2021/5/7
#-------------------------------------------------------------------------------
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        #注意每次Prev指向颠倒的前面，prev.next表示等待颠倒的结点
        #循环的时候记录三个指针，使用prev,a,b，
        prev,prev.next = self,head
        while prev.next and prev.next.next:
            a=prev.next
            b=a.next
            #(1)把prev.next挪动到b点，
            #(2)然后颠倒对应指针
            #(3)把a的结点指向b的后续结点
            prev.next,b.next,a.next = b,a,b.next
            #在ba颠倒后把prev指向a
            prev = a
        return self.next #注意这里返回该链表self.next