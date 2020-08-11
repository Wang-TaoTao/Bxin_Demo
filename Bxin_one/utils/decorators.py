# import pytz
# from datetime import datetime, timedelta
#
# from decimal import Decimal
#
# now = datetime.now()
# day_start_str = '%s-%s-%s 00:00:00' % (now.year, now.month, now.day)
# day_start = datetime.strptime(day_start_str, '%Y-%m-%d %H:%M:%S')
# tz = pytz.timezone('Asia/Shanghai')
# begin = tz.localize(day_start)
# end = begin + timedelta(days=-1)
#
#
# print(begin)
# print(end)
# import pytz
# from datetime import datetime
#
# now = datetime.now().strftime("%Y-%m-%d")
# print(now)
# tz = pytz.timezone('Asia/Shanghai')
# today = tz.localize(now).strftime('%Y-%m-%d')
# print(today)
#
# res_dict = {}
# res_list= []
#
# for i in range(3):
#     key = '{}:{}:{}:{}'.format(1, 'btc', '群',i)
#     data = res_dict.get(key,{})
#     data['user_target_id'] = 1
#     data['currency']  = 'btc'
#     data['category'] = '群'
#     data['benefit'] = data.get('benefit', Decimal('0')) + i
#     res_dict[key] = data
#     # print("data:",data)
#     # print('---')
#     # print("res_dict:",res_dict)
#     # print('---')
#
# print(res_dict)

request_envion_mac={'SSH_CONNECTION': '103.233.52.2 58636 172.17.0.8 22', 'LANG': 'en_US.utf8', 'HISTTIMEFORMAT':
'%F %T ', 'OLDPWD': '/home/ubuntu', 'VIRTUAL_ENV': '/home/ubuntu/.local/share/virtualenvs/bixin-permissions-RDDAFReO', 'S_COLORS': 'auto',
'XDG_SESSION_ID': '4974', 'USER': 'ubuntu', 'PIP_PYTHON_PATH': '/usr/bin/python3', 'PWD': '/home/ubuntu/Desktop/bixin-permissions',
'HOME': '/home/ubuntu', 'SSH_CLIENT': '103.233.52.2 58636 22', 'XDG_DATA_DIRS': '/usr/local/share:/usr/share:/var/lib/snapd/desktop',
'PIPENV_ACTIVE': '1', 'SSH_TTY': '/dev/pts/0', 'MAIL': '/var/mail/ubuntu', 'SHELL': '/bin/bash', 'TERM': 'xterm-256color',
'PYTHONDONTWRITEBYTECODE': '1', 'SHLVL': '2', 'PROMPT_COMMAND': 'history -a; history -a; history -a; history -a; history -a; history -a; ',
'LOGNAME': 'ubuntu', 'PIP_DISABLE_PIP_VERSION_CHECK': '1', 'XDG_RUNTIME_DIR': '/run/user/500',
'PATH': '/home/ubuntu/.local/share/virtualenvs/bixin-permissions-RDDAFReO/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin',
'PS1': '(bixin-permissions) ${debian_chroot:+($debian_chroot)}\\u@\\h:\\w\\$ ', 'HISTSIZE': '3000', '_': '/home/ubuntu/.local/share/virtualenvs/bixin-permissions-RDDAFReO/bin/python',
'DJANGO_SETTINGS_MODULE': 'bixin_permissions.settings', 'TZ': 'UTC', 'RUN_MAIN': 'true', 'SERVER_NAME': 'localhost.localdomain',
'GATEWAY_INTERFACE': 'CGI/1.1', 'SERVER_PORT': '8000', 'REMOTE_HOST': '', 'CONTENT_LENGTH': '', 'SCRIPT_NAME': '', 'SERVER_PROTOCOL': 'HTTP/1.0',
'SERVER_SOFTWARE': 'WSGIServer/0.2', 'REQUEST_METHOD': 'GET', 'PATH_INFO': '/', 'QUERY_STRING': '', 'REMOTE_ADDR': '127.0.0.1',
'CONTENT_TYPE': 'text/plain', 'HTTP_HOST': 'permissions.simaiou.com', 'HTTP_CONNECTION': 'close', 'HTTP_CACHE_CONTROL': 'max-age=0',
'HTTP_UPGRADE_INSECURE_REQUESTS': '1', 'HTTP_USER_AGENT': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
'HTTP_ACCEPT': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'HTTP_ACCEPT_ENCODING': 'gzip, deflate', 'HTTP_ACCEPT_LANGUAGE': 'zh-CN,zh;q=0.9', 'wsgi.input': "<django.core.handlers.wsgi.LimitedStream object at 0x7f69f960a668>",
'wsgi.errors': "<_io.TextIOWrapper name='<stderr>' mode='w' encoding='UTF-8'>", 'wsgi.version': "(1, 0)", 'wsgi.run_once': False, 'wsgi.url_scheme': 'http',
'wsgi.multithread': True, 'wsgi.multiprocess': False, 'wsgi.file_wrapper': "<class 'wsgiref.util.FileWrapper'>"}






request_envion_iphone = {'SSH_CONNECTION': '103.233.52.2 58636 172.17.0.8 22', 'LANG': 'en_US.utf8', 'HISTTIMEFORMAT': '%F %T ',
'OLDPWD': '/home/ubuntu', 'VIRTUAL_ENV': '/home/ubuntu/.local/share/virtualenvs/bixin-permissions-RDDAFReO', 'S_COLORS': 'auto', 'XDG_SESSION_ID': '4974',
'USER': 'ubuntu', 'PIP_PYTHON_PATH': '/usr/bin/python3', 'PWD': '/home/ubuntu/Desktop/bixin-permissions', 'HOME': '/home/ubuntu', 'SSH_CLIENT': '103.233.52.2 58636 22',
 'XDG_DATA_DIRS': '/usr/local/share:/usr/share:/var/lib/snapd/desktop', 'PIPENV_ACTIVE': '1', 'SSH_TTY': '/dev/pts/0', 'MAIL': '/var/mail/ubuntu', 'SHELL': '/bin/bash',
  'TERM': 'xterm-256color', 'PYTHONDONTWRITEBYTECODE': '1', 'SHLVL': '2', 'PROMPT_COMMAND': 'history -a; history -a; history -a; history -a; history -a; history -a; ',
  'LOGNAME': 'ubuntu', 'PIP_DISABLE_PIP_VERSION_CHECK': '1', 'XDG_RUNTIME_DIR': '/run/user/500', 'PATH': '/home/ubuntu/.local/share/virtualenvs/bixin-permissions-RDDAFReO/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin',
  'PS1': '(bixin-permissions) ${debian_chroot:+($debian_chroot)}\\u@\\h:\\w\\$ ', 'HISTSIZE': '3000', '_': '/home/ubuntu/.local/share/virtualenvs/bixin-permissions-RDDAFReO/bin/python',
  'DJANGO_SETTINGS_MODULE': 'bixin_permissions.settings', 'TZ': 'UTC', 'RUN_MAIN': 'true', 'SERVER_NAME': 'localhost.localdomain', 'GATEWAY_INTERFACE': 'CGI/1.1',
   'SERVER_PORT': '8000', 'REMOTE_HOST': '', 'CONTENT_LENGTH': '', 'SCRIPT_NAME': '', 'SERVER_PROTOCOL': 'HTTP/1.0', 'SERVER_SOFTWARE': 'WSGIServer/0.2', 'REQUEST_METHOD': 'GET',
   'PATH_INFO': '/favicon.ico', 'QUERY_STRING': '', 'REMOTE_ADDR': '127.0.0.1', 'CONTENT_TYPE': 'text/plain', 'HTTP_HOST': 'permissions.simaiou.com', 'HTTP_CONNECTION': 'close',
   'HTTP_ACCEPT': '*/*', 'HTTP_USER_AGENT': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1 Mobile/15E148 Safari/604.1',
   'HTTP_ACCEPT_LANGUAGE': 'zh-cn', 'HTTP_REFERER': 'http://permissions.simaiou.com/', 'HTTP_ACCEPT_ENCODING': 'gzip, deflate', 'wsgi.input': '<django.core.handlers.wsgi.LimitedStream object at 0x7f69f960ab00>', 'wsgi.errors': "<_io.TextIOWrapper name='<stderr>' mode='w' encoding='UTF-8'>", 'wsgi.version': (1, 0), 'wsgi.run_once': False,
    'wsgi.url_scheme': 'http', 'wsgi.multithread': True, 'wsgi.multiprocess': False, 'wsgi.file_wrapper': "<class 'wsgiref.util.FileWrapper'>"}


user_agent_mac= 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'
user_agent_iphone= 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1 Mobile/15E148 Safari/604.1'
user_agent_iphone_wechat = 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/7.0.12(0x17000c30) NetType/WIFI Language/zh_CN'
user_agent_android_wechat = 'Mozilla/5.0 (Linux; Android 9; INE-AL00 Build/HUAWEIINE-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.120 MQQBrowser/6.2 TBS/045227 Mobile Safari/537.36 MMWEBID/2735 MicroMessenger/7.0.15.1680(0x27000F3B) Process/tools WeChat/arm64 NetType/4G Language/zh_CN ABI/arm64'

# user_version_mac = user_agent_mac.split(' ')
# print(user_version_mac)
#
# user_version_iphone = user_agent_iphone.split(' ')
# print(user_version_iphone)
import re
user_version_iphone_wechat = user_agent_iphone_wechat.split(' ')
for iphone in user_version_iphone_wechat:
    if re.match(r'iPhone', iphone):
        version = str(user_version_iphone_wechat).split(' ')[-3]
        print(version)



user_version_android_wechat = user_agent_android_wechat.split(' ')
for android in user_version_android_wechat:
    if re.match(r'Android', android):
        version = str(user_version_android_wechat).split(' ')[-6]
        print(version)

a = 1
b = 2
c = 0

res = a and b or c
print(res)


import pytz
from datetime import datetime, timedelta
from django.db.models import Q, Sum
d = '2020-06-10'
day_start_str = '{} 00:00:00'.format(d)
day_start = datetime.strptime(day_start_str, '%Y-%m-%d %H:%M:%S')
tz = pytz.timezone('Asia/Shanghai')
begin = tz.localize(day_start)
end = begin + timedelta(days=1)

print(begin)
print(end)