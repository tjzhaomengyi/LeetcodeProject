# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         edit_distance
# Description:  编辑距离,从单词word1变为单词word2，通过Insert\Delete\Replace最少需要多少步
# Author:       zhaomengyi
# Date:         2021/5/23
# NO:LC72
# 解法: (1)字符串匹配统一做法，DP[i][j]其中i表示单词1的字符位，j表示单词2的字符位；word1前i个字符要替换到word2前j个字符，
# 最少需要多少步，最终结果DP[m][n]m表示word1长度，n表示word2长度。
# (2)DP方程，DP[i,j]分为两种情况，if w1[i]==w2[j],DP[i,j]=DP[i-1,j-1]
# else两者不等，需要做三种操作//插入、删除、替换，1+min(DP[i-1,j]删除,DP[i,j-1]增加,DP[i-1,j-1])，1表示该步操作
# 时间复杂度O(m*n)两个单词的长度
#-------------------------------------------------------------------------------
class Solution:
  def minDistance(self, word1: str, word2: str) -> int:
    m,n = len(word1),len(word2)
    dp=[[0 for _ in range(n+1)] for _ in range(m+1)]

    for i in range(m+1):dp[i][0]=i
    for j in range(n+1):dp[0][j]=j

    for i in range(1,m+1):
      for j in range(1,n+1):
        dp[i][j]=min(dp[i-1][j-1]+(0 if word1[i-1] == word2[j-1] else 1),
                     dp[i-1][j]+1,
                     dp[i][j-1]+1)

    return dp[m][n]
