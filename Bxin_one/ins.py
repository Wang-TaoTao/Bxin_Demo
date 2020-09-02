import re

import math

import pytz

from Bxin_one.settings import BASE_DIR

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

import random
def random_recommend_text():
    text_list = [u'「币信」安全好用的区块链钱包推荐给你',
                 u'终于有一款区块链钱包能够配得上我的身份，安全又好用，推荐给你哟~ ',
                 u'你身边优秀的BTCer邀请你使用安全好用的区块链「币信钱包」',
                 u'优秀的BTCer必备的「币信」区块链钱包等你来使用哦～',
                 u'(๑̀ㅂ•́)و✧ 朋友间最好的默契，就是你跟我用同样的「币信」区块链钱包咩',
                 ]
    return random.choice(text_list)


xx = random_recommend_text()
res = xx +'\\n' + 'https://bixin.im/landing_page/?i=GULT3S#/'

print(res)

import datetime

today = datetime.date.today()
# today = today.strftime('%Y-%m-%d 00:00:00')
print(today)

abc = today + datetime.timedelta(days=1)
print(abc.strftime('%Y-%m-%d 00:00:00'))
import os
print(os.path.join(BASE_DIR))
# STATICFILES_DIRS = os.path.join(BASE_DIR, 'static')
# STATICFILES_IMAGES = os.path.join(STATICFILES_DIRS, 'images')
#
# print(STATICFILES_DIRS)
# print(STATICFILES_IMAGES)

