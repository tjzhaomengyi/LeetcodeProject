# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         valid_parentheses
# Description:  判断字符串的括号是否合法
# Author:       zhaomengyi
# Date:         2021/5/8
# TimeCom:O(n),SpaceCom:O(n)
# NO.LC20
#-------------------------------------------------------------------------------
class Solution:
    def isValid(self, s: str) -> bool:
        #把左括号放入栈中，出现匹配的右括号就弹出
        stack=[]
        paren_map = {')':'(',']':'[','}':'{'}
        for c in s:
            # if c in paren_map.values():
            #     stack.append(c)
            # elif c in paren_map.keys() and stack:
            #     top = stack[-1]
            #     if top == paren_map[c]:
            #         stack.pop()
            #     else:
            #         return False
            # elif c in paren_map.keys() and not stack:
            #     return False
            if c not in paren_map.keys():
                stack.append(c)
            elif not stack or paren_map[c]!=stack.pop():
                return False
        return not stack

if __name__ == '__main__':
    test = Solution()
    #print(test.isValid(s='()[]{}'))
    print(test.isValid(s='(])'))