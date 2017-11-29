"""
Generate random password, including letters, numbers, and special characters.

2017-11-30, yanwei
"""

import random
import string
import sys

include_lower_letters = True
include_upper_letters = True
include_numbers = True

special_char_num = 1  # use fewer special char instead of random to simplify password inputting
special_chars = r'`~!@#$%^&*()-_=+[{]}\\|;:\'\",<.>/?'

pswd_len = 16  # total length of the password

if special_char_num >= pswd_len:
    print('特殊字符数不能超过密码总长度！')
    sys.exit(0)

candidate_chars = []

if include_lower_letters:
    for c in string.ascii_lowercase:
        candidate_chars.append(c)

if include_upper_letters:
    for c in string.ascii_uppercase:
        candidate_chars.append(c)

if include_numbers:
    for c in string.digits:
        candidate_chars.append(c)

for total in range(10):
    password = []

    for i in range(pswd_len - special_char_num):
        index = random.randrange(0, len(candidate_chars))
        password.append(candidate_chars[index])

    for i in range(special_char_num):
        index1 = random.randrange(0, len(special_chars))
        index2 = random.randrange(0, len(password))
        password.insert(index2, special_chars[index1])

    print(''.join(password))
