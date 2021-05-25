# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         stock_buy
# Description:  股票买卖
# Author:       zhaomengyi
# Date:         2021/5/21
# NO:LC121、LC122、LC123、LC309
# 解法：121循环一次记录遍历的最小值，然后新的值减去之前的最小值，得到最大利润
# 用一个DP方法，解决上面这些所有问题
# k表示股票可以交易的次数，
#（1）定义DP，MP[i],到第i天的最大利润；
# a.在第i天可以买入股票： MP[i] = MP[i-1]+(-a[i])在第i天买入股票；
# b.在第天可以卖出股票：MP[i] = MP[i-1]+a[i]
# 但是用这种简单的公式是不行的，需要记录当前是否持有股票MP[i]增加一个维度MP[i][j],j=0表示手头没有股票；j=1表示用于股票
# MP[i,0]第i天没有股票的最大值可以是前一天没有股票的最大利润Mp[i-1,0]也可以是前一天拥有在第i天卖出MP[i-1,1]+a[i],选择这两个值的最大值
# MP[i,1]=max(MP[i-1,1]不动,MP[i-1,0]-a[i]买入)
# 通过这个可以解决买入一次121和买入无数次122的的问题
# 如果交易股票次数是k那么还要判断i是否大于k，那么还要给DP[i][j]再加以为交易次数的维度DP[i][j][k]
# 这个面试已经就到这个三维的DP了
# MP[i,k,0] = max(MP[i-1,k,0]不动,MP[i-1,k-1,1]+a[i]卖)得到新的一天当天交易k次没有股票
# MP[i,k,1] = max(MP[i-1,k-1,0]-a[i]买入,MP[i-1,k,0]不动)
# 求MP[n-1,{0,k},0]的值
# 拓展如果手中可以有某个股票多只，这时候需要把j表示为0到x，状态变为三种：
# MP[i,k,j] = max(MP[i-1,k,j]不动,MP[i-1,k-1,j+1]+a[i]卖,MP[i-1,k-1,j-1]-a[i]买)
# 时间复杂度O(N*K)
# 也可以使用变量来维护递推，但是这样的话扩展性不太好，可以使用变量来定义状态，可读性好一些
#-------------------------------------------------------------------------------
import sys
from typing import List

from conda_build.os_utils.pyldd import maxint


class Solution:
  #最多进行一次买卖，第二维度0-没有买入股票；1-买入或者已经买入股票持仓了 2-买入了一股现在已经卖了
  #LC121,某天买完了，某天卖，就1次
  def maxProfit_121(self, prices: List[int]) -> int:
    if not prices: return 0
    res =0
    profit = [[0 for i in range(3)] for i in range(len(prices))]
    profit[0][0],profit[0][1],profit[0][2] = 0,-prices[0],0

    for i in range(1,len(prices)):
      profit[i][0] = profit[i-1][0] #第i天没有买入
      profit[i][1] = max(profit[i-1][1],profit[i-1][0]-prices[i])#第i天买入或者已经买入了股票
      profit[i][2] = profit[i-1][1]+prices[i]#第i天卖出股票
      res = max(res,profit[i][0],profit[i][1],profit[i][2])

    return res
  #LC123，就是交易两次，但是不能同时持仓，最多可以完成两笔交易k=2表示可以交易两次，三维数组表示：第i天；交易次数；持仓状态
  def maxProfit_K(self,prices:List[int]) -> int:
    if not prices: return 0

    profit = [[[0 for _ in range(2)] for _ in range(3)] for _ in range(len(prices))]

    profit[0][0][0],profit[0][0][1] = 0,-prices[0] #表示第一天不持有或者买入
    profit[0][1][0],profit[0][1][1] = -sys.maxsize,-sys.maxsize
    profit[0][2][0],profit[0][2][1] = -sys.maxsize,-sys.maxsize

    for i in range(1,len(prices)):
      #我们把一次完整的交易叫做一次交易，就是先买再卖
      #1、没有完成一次交易的时候
      profit[i][0][0] = profit[i-1][0][0] #没有完成一次交易
      profit[i][0][1] = max(profit[i-1][0][1],profit[i-1][0][0]-prices[i])# 前一天有持仓不动，前一天无持仓买入

      #完成一次买入的情况
      profit[i][1][0] = max(profit[i-1][1][0],profit[i-1][0][1]+prices[i])#交易了一次但是无持仓:不动，或者当天卖
      profit[i][1][1] = max(profit[i-1][1][1],profit[i-1][1][0]-prices[i])#当前持仓交易一次，或者买入

      #完成两次交易
      profit[i][2][0] = max(profit[i-1][2][0],profit[i-1][1][1]+prices[i])

    end = len(prices)-1
    return max(profit[end][0][0],profit[end][1][0],profit[end][2][0])

if __name__ == '__main__':
    print(Solution().maxProfit_K([1,2,3,4,5]))