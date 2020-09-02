# # 获取时区对象
# import datetime
#
# import pytz
#
# tz_utc_8 = pytz.timezone('Asia/Shanghai')
# # 根据时区获取当前时间
# now = datetime.datetime.now(tz_utc_8)
#
# print(now.time())
# print(type(now.time()))
#
#
# print(now.time().strftime('%H:%M:%S'))
# if now.time().strftime('%H:%M:%S') == '15:36:50':
#     print('True')


