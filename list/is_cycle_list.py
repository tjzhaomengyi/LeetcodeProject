# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         is_cycle_list
# Description:
# Author:       zhaomengyi
# Date:         2021/5/7
#-------------------------------------------------------------------------------
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        #快慢指针都指向头结点
        fast = slow = head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False