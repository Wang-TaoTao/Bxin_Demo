import pyotp
import qrcode
from PIL import Image, ImageDraw

# 生成密钥
# sec =  pyotp.random_base32()
sec = 'MZUHK7QJKUCJY3EB'
print('sec',sec)

# 这里生成一个基于时间的otp对象    # 基于计数器的otp对象是HOTP
topt = pyotp.TOTP(sec)
print('topt',topt)

# # 获取二维码uri
# qr_uri = pyotp.totp.TOTP(sec).provisioning_uri('test')
# # 生成二维码
# img = qrcode.make(qr_uri)
# # 显示二维码
# img.get_image().show()


import time
#time.sleep(30)

res = topt.verify(144987)
print(res)



