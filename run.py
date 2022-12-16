#!/usr/bin/env python3
# -*- coding = utf-8 -*-
import subprocess

def mode(mode):
    if mode == 'train':
        map_use = input('please input the map file:\n> ')
        episodes = input('please input the times you want to train(default 30000)\n> ')
        print(subprocess.call('python ./train.py --level ' + map_use + ' --num-episodes ' + episodes, shell=True))
    elif mode == 'play':
        module = input('please input the module you use:\n> ')
        map_use = input('please input the map file:\n> ')
        print(subprocess.call('python ./play.py --interface gui --agent dqn --model ' + module + ' --level ' + map_use +' --num-episodes 10', shell=True))
    elif mode == 'deps':
        print(subprocess.call('python -m pip install -i https://pypi.tuna.tsinghua.edu.cn/simple --upgrade -r requirements.txt'))
    elif mode == 'help':
        print('mode choice:\ntrain play deps(install the depends)')

if __name__ == '__main__':
    while True:
        mode_use = input('please input a mode:\nuse help for more information\n')
        mode(mode_use)
