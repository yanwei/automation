import tinify

tinify.key = 'rVpv97zHq3Xd70lk1hx5KbD6dfLs7zSt'
tinify.proxy = 'http://127.0.0.1:1087'

source = tinify.from_file('/Users/yanwei/PycharmProjects/automation/teacher-resource-hub.png')
source.to_file('/Users/yanwei/PycharmProjects/automation/teacher-resource-hub-new.png')
