import os
import re

application_path = '/Applications'
cmd_template = 'plutil -p /Applications/{}/Contents/Info.plist | grep CFBundleShortVersionString'

for item in os.listdir(application_path):
    if re.match(r'.*\.app$', item):
        cmd = cmd_template.format(item)
        print(os.popen(cmd).read())
