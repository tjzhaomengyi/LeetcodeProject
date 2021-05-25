# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         myqueue
# Description:
# Author:       zhaomengyi
# Date:         2021/5/9
#-------------------------------------------------------------------------------
# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         myqueue
# Description:
# Author:       zhaomengyi
# Date:         2021/5/9
#-------------------------------------------------------------------------------
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.input_stack = []
        self.output_stack = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.input_stack.append(x)


    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.input_stack is None and self.output_stack is None:
            return None
        else:
            for i in range(0,len(self.input_stack)):
                self.output_stack.append(self.input_stack.pop())
        return self.output_stack.pop()


    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.input_stack is None and self.output_stack is None:
            return None
        else:
            for i in range(0, len(self.input_stack)):
                self.output_stack.append(self.input_stack.pop())
        return self.output_stack[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if len(self.input_stack)==0 and len(self.output_stack)==0:
            return True
        else:
            return False



# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(None)
obj.push(1)
obj.push(2)
obj.push(3)
obj.push(4)
obj.push(None)
obj.push(5)
obj.push(None)
# obj.push("b")
# obj.push("c")

# param_3 = obj.peek()
# param_2 = obj.pop()
param_4 = obj.empty()
print(obj.pop(),obj.pop(),obj.pop(),obj.pop(),obj.pop())