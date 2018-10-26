"""
更新所有pip包。
由于pip命令不支持更新全部，所以写一个循环，对每个包调用upgrade命令。

2017-11-27, yanwei, pip 9.0.1
2018-05-05, yanwei, support pip 10.0.1
"""

import json
import os

package_list = json.loads(os.popen('pip3 list --outdated --format json').readlines()[0])

for package in package_list:
    os.system('pip3 install -U ' + package['name'])
