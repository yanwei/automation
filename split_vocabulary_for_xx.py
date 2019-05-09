import openpyxl
import re

file_path = '/Users/yanwei/Desktop/中考词汇手册.xlsx'
file_path_new = '/Users/yanwei/Desktop/中考词汇手册(new).csv'

wb = openpyxl.load_workbook(file_path)
ws = wb['Sheet2']

fn = open(file_path_new, 'wt')

count = 0
for row in ws.rows:
    count += 1
    # if count > 5:
    #     break

    line = row[0].value
    word = ''
    for w in line.split():
        if re.match(r'^[A-Za-z()]+$', w):
            word += w
            word += ' '
        else:
            break

    explain = line[len(word):]
    print(word, '|', explain)
    fn.write(word + '|' + explain + '\n')

fn.close()
