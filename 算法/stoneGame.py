#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   stoneGame.py
@Time    :   2019/12/14 15:25:44
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   
亚历克斯和李用几堆石子在做游戏。偶数堆石子排成一行，每堆都有正整数颗石子 piles[i] 。

游戏以谁手中的石子最多来决出胜负。石子的总数是奇数，所以没有平局。

亚历克斯和李轮流进行，亚历克斯先开始。 每回合，玩家从行的开始或结束处取走整堆石头。 这种情况一直持续到没有更多的石子堆为止，此时手中石子最多的玩家获胜。

假设亚历克斯和李都发挥出最佳水平，当亚历克斯赢得比赛时返回 true ，当李赢得比赛时返回 false 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/stone-game
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# here put the import lib
from typing import List
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        return True
if __name__ == '__main__':
    s = Solution()
    print(s.stoneGame([5,3,4,5]))