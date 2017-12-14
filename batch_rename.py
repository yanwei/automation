import os
import re

path = '/Users/yanwei/Downloads'
new_prefix = '火柴棒'
rename_count = 0

for item in os.listdir(path):
    if os.path.isfile(os.path.join(path, item)):
        # 只改名特定命名规则的文件，如数字开头，.png结尾
        if re.match(r'^\d\w+\.png$', item):  # 数字开头，.png结尾的文件名
            # 生成新的文件名
            newname = re.sub(r'^[\d]+', new_prefix, item)
            # 进行改名操作
            os.rename(os.path.join(path, item), os.path.join(path, newname))
            rename_count += 1
            print(item, '-->', newname)

print(rename_count, 'files renamed.')
