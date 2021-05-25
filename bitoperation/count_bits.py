# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         count_bits
# Description:  给定一个正整数，计算其中每个正整数的2进制位数，并用数组返回
# Author:       zhaomengyi
# Date:         2021/5/20
# NO:LC338
# 解法：找里面有多少个1，如果给n=2，返回[0,1,1]。开一个长度为n的数组，然后暂存0，count[i]=count[i&(i-1)]+1
# count[i&(i-1)]表示去除最低位之后有多少个1
#-------------------------------------------------------------------------------
from typing import List


class Solution:
  def countBits(self, num: int) -> List[int]:
    res=[0]*(num+1)
    for i in range(1,num+1):
      res[i] = res[i&(i-1)]+1#这里很巧妙，比如到4的时候0100，这个时候去掉最后一个1是0，0的结果存在再加1得结果
    return res

if __name__ == '__main__':
    res = Solution().countBits(2)
    print(res)