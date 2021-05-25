# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         ${NAME}
# Description:  反转链表
# Author:       ${USER}
# Date:         ${DATE}
#-------------------------------------------------------------------------------
class Revers_Linked_List:
    def reverseList(self,head):
        #前指针指向空，后指针指向头指针
        cur,prev = head,None
        while cur:
            cur.next,prev,cur = prev,cur,cur.next
        return prev
