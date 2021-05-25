# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         priorityqueue
# Description:  优先队列,根据属性进行出队
# Author:       zhaomengyi
# Date:         2021/5/9
# 优先队列实现机制：（1）用Heap堆(Binary\Binomial\Fibonacci)大顶堆和小顶堆实现优先队列很少了（2）Binary Search Tree
# NO:LC703 K Largest
# 解法（1）对每次进来的值记录前K个最大 （2）每次进来数进行排序O(N*KLogK) (3)使用优先队列
# 思路：使用小顶堆，达到O(1)的时间复杂度进行查找第N大的值，如果比堆顶小，那么就没法进行堆，单次入队调整的时间复杂度是O(log2k)
# Java中默认的PriorityQueue的实现就是小顶堆
#-------------------------------------------------------------------------------
from typing import List
from heapq import *

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        heapify(nums)
        klarage = nlargest(self.k,nums)
        heapify(klarage)
        self.hq = klarage


    def add(self, val: int) -> int:
        if len(self.hq) < self.k:
            heappush(self.hq,val)
        elif val > self.hq[0]:
            heapreplace(self.hq,val)
        return self.hq[0]


if __name__ == '__main__':

# Your KthLargest object will be instantiated and called as such:
    obj = KthLargest(3, [4,5,8,2])
    obj.add(3)
    obj.add(5)
    obj.add(10)
    obj.add(9)
    obj.add(4)
    print(obj)