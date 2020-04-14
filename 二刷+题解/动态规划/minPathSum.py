#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   minPathSum.py
@Time    :   2020/04/13 19:39:40
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :
给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。

示例:

输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 7
解释: 因为路径 1→3→1→1→1 的总和最小。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-path-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# here put the import lib
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[float('inf')] * (n+1) for _ in range(m+1)]
        dp[0][1] = 0
        for col in range(1, m+1):
            for raw in range(1, n+1):
                dp[col][raw] = min(dp[col-1][raw], dp[col][raw-1]) + grid[col-1][raw-1]
        return dp[-1][-1]

if __name__ == '__main__':
    s = Solution()
    c = s.minPathSum([[1,3,1],[1,5,1],[4,2,1]])
    print(c)