# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         sliding_window
# Description:  求滑动窗口的最大值
# Author:       zhaomengyi
# Date:         2021/5/10
# NO:LC239，hard,这个逻辑挺恶心
# 解法：（1）优先队里，每次找最大值，用大顶堆，每次滑动维护这个堆：删除离开的元素，加入新来的元素，取出堆顶元素
#   查找O(1),进入的时候是logk，总体是O(nlogk)
#   (2)时间复杂度O(n),因为是固定大小的窗口，可以简化，不用堆，用双端队列deque。前K个元素加到队列，新元素进来进行维护：
#   a.[1,3,-1,-3,5,3,6]，先把1放入队列，然后放3，当3进来的时候，1<3，出队，-1进来双端队列[3,-1,-3],5进来，
#-------------------------------------------------------------------------------
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window,res = [],[]#window存下标，res存结果
        for i,x in enumerate(nums):
            if i>=k and window[0]<=i-k:
                window.pop(0)
            while window and nums[window[-1]]<=x: #通过遍历window下标，和新进来的进行比较
                window.pop()
            window.append(i)
            if i>=k-1: #最后维护结果表
                res.append(nums[window[0]])
        return res

if __name__ == '__main__':
    obj = Solution()
    a=obj.maxSlidingWindow([1],1)
    b=obj.maxSlidingWindow([1,-1],1)
    c=obj.maxSlidingWindow([9,11],2)
    d=obj.maxSlidingWindow([4,-2],2)
    print(a,b,c,d)
