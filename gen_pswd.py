"""
Generate random password, including letters, numbers, and special characters.

2017-11-30, yanwei
"""

import random
import string


class PasswordGenerator:
    def __init__(self, pswd_len, include_lower_letters, include_upper_letters, include_numbers, special_char_num):
        self.pswd_len = pswd_len
        self.include_lower_letters = include_lower_letters
        self.include_upper_letters = include_upper_letters
        self.include_numbers = include_numbers
        # use fewer special char instead of random to simplify password inputting
        self.special_char_num = special_char_num

        self.candidate_chars = []

        if self.include_lower_letters:
            for c in string.ascii_lowercase:
                self.candidate_chars.append(c)

        if self.include_upper_letters:
            for c in string.ascii_uppercase:
                self.candidate_chars.append(c)

        if self.include_numbers:
            for c in string.digits:
                self.candidate_chars.append(c)

        self.special_chars = r'`~!@#$%^&*()-_=+[{]}\\|;:\'\",<.>/?'

    def random_pswd(self):
        if self.special_char_num >= self.pswd_len:
            return '特殊字符数不能超过密码总长度！'

        pswd_list = []

        for _ in range(self.pswd_len - self.special_char_num):
            index = random.randrange(0, len(self.candidate_chars))
            pswd_list.append(self.candidate_chars[index])

        for _ in range(self.special_char_num):
            index1 = random.randrange(0, len(self.special_chars))
            index2 = random.randrange(0, len(pswd_list))
            pswd_list.insert(index2, self.special_chars[index1])

        return ''.join(pswd_list)


if __name__ == '__main__':
    pg = PasswordGenerator(16, True, True, True, special_char_num=1)
    for i in range(10):
        print(pg.random_pswd())
