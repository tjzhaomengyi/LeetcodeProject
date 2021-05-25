# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         power
# Description:  幂指数运算
# Author:       zhaomengyi
# Date:         2021/5/18
# NO:LC50
# 解法：分治算法，一半一半算
#-------------------------------------------------------------------------------
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if not n:return 1
        if n<0:
           return 1/self.myPow(x,-n) #如果是负数倒过来算
        if n%2: #如果是基数减1再算
            return x*self.myPow(x,n-1)
        return self.myPow(x*x,n/2) #正偶数的话直接折半

if __name__ == '__main__':
    print(Solution().myPow(2,10))