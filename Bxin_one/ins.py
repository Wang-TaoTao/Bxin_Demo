import re

import math

a = u'5b907dda36944958af373e5b24ce215a'
print(a.encode().decode())
username = '15041890905'


phone_pas = username[3:7]

res = username.replace(phone_pas,'****')

print(res)


def card_number_hidden(card_number):


    card_number_1 = card_number[7:15]

    # card_number = card_number[2:5]
    #
    # card_number = card_number[3:7]
    hidden_card = card_number.replace(card_number_1, '*' * len(card_number_1))
    return hidden_card

re = card_number_hidden('21090219980901301X')
print(re)

file_r = open('country_code_zh.py')
r = file_r.readline()
print(r)

from decimal import Decimal

if Decimal('0.01') < Decimal('0.011'):
    print('1')

res = Decimal('0.01') / 100000000
print(res)


ss = '\u6fb3\u95e8'.encode().decode()
print(ss)


demo1 = '\u547c\u98ce\u5524\u96e812'
print(demo1.encode().decode())



class Cat(object):

    def __init__(self):
        self.name = "jn"

    def __getattr__(self, item):
        return "tm"


cat = Cat()
print(cat.name)
print(getattr(cat, 'name'))
print("*" * 20)
print(cat.age)
print(getattr(cat, 'age'))


demo2 = 1246.87

print(math.ceil(demo2))