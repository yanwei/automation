"""
更新所有pip包。
由于pip命令不支持更新全部，所以写一个循环，对每个包调用upgrade命令。

2017-11-27, yanwei
"""

import os
import re

for line in os.popen('pip3 list').readlines():
    if re.match(r'[\w-]+ \([\d\.]+\)$', line):
        os.system('pip3 install --upgrade ' + line.split(' ')[0])
