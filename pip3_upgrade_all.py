"""
更新所有pip包。
由于pip命令不支持更新全部，所以写一个循环，对每个包调用upgrade命令。

2017-11-27, yanwei, pip 9.0.1
2018-05-05, yanwei, support pip 10.0.1
"""

import json
import os

package_list = json.loads(
    os.popen('pip3 list --outdated --format json').readlines()[0])

updated_packages = []

for package in package_list:
    os.system('pip3 install -U ' + package['name'])
    updated_packages.append(package['name'])

if len(updated_packages) == 0:
    print('All the packages are up to date.')
else:
    print('-' * 80)
    print('Successfully updated {} packages: {}'.format(len(updated_packages), ', '.join(updated_packages)))
