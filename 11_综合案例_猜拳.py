#!/usr/bin/env pytho      
# -*- coding: utf-8 -*-
import random

# 1.出拳
# 玩家
res = ['石头', '布', '剪刀']
player = int(input('请出拳：0--石头，1--布，2--剪刀\n'))
print(f'您稍加思索，出了{res[player]}。')

# 电脑
computer = random.randint(0, 2)  # 包含边界
print(f'您的对手思索半天，出了{res[computer]}。')

# 2.判断输赢
if player == 0:
    if computer == 0:
        print('平局！有种别走再来一把。')
    elif computer == 1:
        print('很遗憾，您输了。')
    else:
        print('恭喜获胜！')
elif player == 1:
    if computer == 1:
        print('平局！有种别走再来一把。')
    elif computer == 2:
        print('很遗憾，您输了。')
    else:
        print('恭喜获胜！')
else:
    if computer == 2:
        print('平局！有种别走再来一把。')
    elif computer == 0:
        print('很遗憾，您输了。')
    else:
        print('恭喜获胜！')
print('Game Over')
