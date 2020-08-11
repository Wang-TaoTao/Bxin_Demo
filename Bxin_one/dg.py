# data = [{'display_name': u'\u5145\u503c\u5f00\u5173', 'weight': 100, 'value': u'open', 'name': '_can_deposit'},
#         {'display_name': u'\u5c0f\u989d\u5b58\u6b3e\u8fb9\u754c(\u4f4e\u4e8e\u6b64\u503c\u5f00\u59cb\u6536\u53d6\u5c0f\u989d\u7ba1\u7406\u8d39\uff09', 'weight': 101, 'value': None, 'name': 'small_deposit_amount'},
#         {'display_name': u'\u5c0f\u989d\u5b58\u6b3e\u7ba1\u7406\u8d39', 'weight': 102, 'value': None, 'name': 'small_deposit_fee'}, 'line',
#         {'display_name': u'\u63d0\u73b0\u5f00\u5173', 'weight': 200, 'value': u'open', 'name': '_can_withdraw'},
#         {'display_name': u'\u7ad9\u5916\u5355\u6b21\u4eba\u8138\u9a8c\u8bc1\u9650\u989d', 'weight': 203, 'value': '', 'name': 'withdraw_once_face_verify_amount'},
#         {'display_name': u'\u7ad9\u591624\u5c0f\u65f6\u4eba\u8138\u9a8c\u8bc1\u9650\u989d', 'weight': 204, 'value': '', 'name': 'withdraw_24h_face_verify_amount'},
#         {'display_name': u'\u7ad9\u591624\u5c0f\u65f6\u4eba\u5de5\u5ba1\u6838\u9650\u989d', 'weight': 205, 'value': '', 'name': 'withdraw_24h_admin_approval_amount'}, {'display_name': u'\u63d0\u73b0\u624b\u7eed\u8d39', 'weight': 206, 'value': '', 'name': 'withdraw_bestfee'}, 'line',
#         {'display_name': u'\u7ad9\u5185\u6700\u5c0f\u8f6c\u8d26\u6570\u91cf', 'weight': 301, 'value': '0.0015', 'name': 'min_transfer_amount'},
#         {'display_name': u'\u7ad9\u5185\u8f6c\u8d26\u5355\u6b21\u4eba\u8138\u9a8c\u8bc1\u9650\u989d', 'weight': 302, 'value': '', 'name': 'transfer_once_face_verify_amount'}, {'display_name': u'\u7ad9\u5185\u8f6c\u8d2624h\u4eba\u5de5\u5ba1\u6838\u9650\u989d', 'weight': 303, 'value': '', 'name': 'transfer_24h_admin_approval_amount'}, {'display_name': u'\u7ad9\u5185\u8f6c\u8d2624h\u4eba\u8138\u9a8c\u8bc1\u9650\u989d', 'weight': 305, 'value': '', 'name': 'transfer_24h_face_verify_amount'}, 'line', {'display_name': u'\u62c5\u4fdd\u4ea4\u6613\u4e0b\u9650', 'weight': 400, 'value': '0.0015', 'name': 'min_escrow_amount'}, {'display_name': u'\u62c5\u4fdd\u4ea4\u6613\u624b\u7eed\u8d39\u7387', 'weight': 410, 'value': None, 'name': 'escrow_fee_rate'}, 'line', {'display_name': u'\u5355\u4e2a\u7ea2\u5305\u4e0a\u9650', 'weight': 501, 'value': '15', 'name': 'redpacket_max_amount'}, {'display_name': u'\u5355\u4e2a\u7ea2\u5305\u4e0b\u9650', 'weight': 502, 'value': '0.00015', 'name': 'redpacket_min_amount'}, 'line', {'display_name': u'\u573a\u5916\u4ea4\u6613\u8d39\u7387', 'weight': 710, 'value': None, 'name': 'flash_escrow_fee_rate'}, 'line', {'display_name': u'\u63d0\u73b0\u624b\u7eed\u8d39\u56e0\u5b50', 'weight': 810, 'value': u'1', 'name': 'withdraw_fee_factor'}]
#
# for i in data:
#     print(i['display_name'].encode().decode())
#




params = [
            {
                "currency": "BTC",
                "unit": "sats",
                "quota_amount": 50000,
                "is_active": True
            },{
                "currency": "BTC",
                "unit": "BTC",
                "quota_amount": 0.005,
                "is_active": True
            }, {
                "currency": "BTC",
                "unit": "BTC",
                "quota_amount": 1,
                "is_active": True
            }
        ]


for p in params:
    if p['unit']=='sats':
        p['quota_amount']=p['quota_amount'] / 100000000
        print(p['quota_amount'])
        params.sort(key=lambda k:(k.get('quota_amount')))
        p['quota_amount'] = p['quota_amount'] * 100000000

print(params)