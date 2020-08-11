# -*- encoding: utf-8 -*-
from decimal import Decimal

country_code_map = {'60': '马来西亚',
                    '63': '菲律宾',
                    '66': '泰国',
                    '81': '日本',
                    '84': '越南',
                    '852': '香港',
                    '855': '柬埔寨',
                    '86': '中国',
                    '880': '孟加拉国',
                    '91': '印度',
                    '93': '阿富汗',
                    '95': '缅甸',
                    '961': '黎巴嫩',
                    '963': '叙利亚',
                    '965': '科威特',
                    '968': '阿曼',
                    '973': '巴林',
                    '975': '不丹',
                    '977': '尼泊尔',
                    '7': '俄罗斯',
                    '31': '荷兰',
                    '33': '法国',
                    '350': '直布罗陀',
                    '352': '卢森堡',
                    '354': '冰岛',
                    '356': '马耳他',
                    '358': '芬兰',
                    '336': '匈牙利',
                    '338': '南斯拉夫',
                    '223': '圣马力诺',
                    '40': '罗马尼亚',
                    '4175': '列支敦士登',
                    '44': '英国',
                    '46': '瑞典',
                    '48': '波兰',
                    '20': '埃及',
                    '213': '阿尔及利亚',
                    '218': '利比亚',
                    '221': '塞内加尔',
                    '223': '马里',
                    '225': '科特迪瓦',
                    '227': '尼日尔',
                    '229': '贝宁',
                    '231': '利比里亚',
                    '233': '加纳',
                    '235': '乍得',
                    '237': '喀麦隆',
                    '239': '圣多美',
                    '240': '赤道几内亚',
                    '242': '刚果',
                    '244': '安哥拉',
                    '247': '阿森松',
                    '249': '苏丹',
                    '251': '埃塞俄比亚',
                    '253': '吉布提',
                    '255': '坦桑尼亚',
                    '257': '布隆迪',
                    '260': '赞比亚',
                    '262': '留尼旺岛',
                    '264': '纳米比亚',
                    '266': '莱索托',
                    '268': '斯威士兰',
                    '27': '南非',
                    '297': '阿鲁巴岛',
                    '1': '美国',
                    '1808': '中途岛',
                    '1808': '威克岛',
                    '1809': '维尔京群岛',
                    '1809': '波多黎各',
                    '1809': '巴哈马',
                    '1907': '阿拉斯加',
                    '500': '福克兰群岛',
                    '502': '危地马拉',
                    '504': '洪都拉斯',
                    '506': '哥斯达黎加',
                    '509': '海地',
                    '52': '墨西哥',
                    '54': '阿根廷',
                    '56': '智利',
                    '58': '委内瑞拉',
                    '592': '圭亚那',
                    '594': '法属圭亚那',
                    '596': '马提尼克',
                    '598': '乌拉圭',
                    '61': '澳大利亚',
                    '671': '关岛',
                    '6723': '诺福克岛',
                    '674': '瑙鲁',
                    '677': '所罗门群岛',
                    '679': '斐济',
                    '683': '纽埃岛',
                    '685': '西萨摩亚',
                    '688': '图瓦卢',
                    '62': '印度尼西亚',
                    '65': '新加坡',
                    '673': '文莱',
                    '82': '韩国',
                    '850': '朝鲜',
                    '853': '澳门',
                    '856': '老挝',
                    '886': '台湾',
                    '90': '土耳其',
                    '92': '巴基斯坦',
                    '94': '斯里兰卡',
                    '960': '马尔代夫',
                    '962': '约旦',
                    '964': '伊拉克',
                    '966': '沙特阿拉伯',
                    '972': '以色列',
                    '974': '卡塔尔',
                    '976': '蒙古',
                    '98': '伊朗',
                    '30': '希腊',
                    '32': '比利时',
                    '34': '西班牙',
                    '351': '葡萄牙',
                    '353': '爱尔兰',
                    '355': '阿尔巴尼亚',
                    '357': '塞浦路斯',
                    '359': '保加利亚',
                    '49': '德国',
                    '39': '意大利',
                    '396': '梵蒂冈',
                    '41': '瑞士',
                    '43': '奥地利',
                    '45': '丹麦',
                    '47': '挪威',
                    '210': '摩洛哥',
                    '216': '突尼斯',
                    '220': '冈比亚',
                    '222': '毛里塔尼亚',
                    '224': '几内亚',
                    '226': '布基拉法索',
                    '228': '多哥',
                    '230': '毛里求斯',
                    '232': '塞拉利昂',
                    '234': '尼日利亚',
                    '236': '中非',
                    '238': '佛得角',
                    '239': '普林西比',
                    '241': '加蓬',
                    '243': '扎伊尔',
                    '245': '几内亚比绍',
                    '248': '塞舌尔',
                    '250': '卢旺达',
                    '252': '索马里',
                    '254': '肯尼亚',
                    '256': '乌干达',
                    '258': '莫桑比克',
                    '261': '马达加斯加',
                    '263': '津巴布韦',
                    '265': '马拉维',
                    '267': '博茨瓦纳',
                    '269': '科摩罗',
                    '290': '圣赫勒拿',
                    '298': '法罗群岛',
                    '1': '加拿大',
                    '1808': '夏威夷',
                    '1809': '安圭拉岛',
                    '1809': '圣卢西亚',
                    '1809': '牙买加',
                    '1809': '巴巴多斯',
                    '299': '格陵兰岛',
                    '501': '伯利兹',
                    '503': '萨尔瓦多',
                    '505': '尼加拉瓜',
                    '507': '巴拿马',
                    '51': '秘鲁',
                    '53': '古巴',
                    '55': '巴西',
                    '57': '哥伦比亚',
                    '591': '玻利维亚',
                    '593': '厄瓜多尔',
                    '595': '巴拉圭',
                    '597': '苏里南',
                    '64': '新西兰',
                    '6722': '科科斯岛',
                    '6724': '圣诞岛',
                    '676': '汤加',
                    '678': '瓦努阿图',
                    '682': '科克群岛',
                    '684': '东萨摩亚',
                    '686': '基里巴斯'}

def country_oto_code(country='', code='0'):

    for cid, message in country_code_map.items():
        if message == country or cid == code:
            code = cid
            country = message
    return {
        'country':country,
        'code': code
    }

res =country_oto_code(code='6722')

print(res.get('country'))

def vformat(value, digits=8):
    fmt = '%%i.%%0%di' % digits
    k = pow(10, digits)

    sign = ''
    if value < 0:
        value = -value
        sign = '-'

    upv = value * k

    r = fmt % (upv // k, upv % k)
    r = sign + r.rstrip('0').rstrip('.')
    if r == '-0':
        r = '0'
    return r


data = Decimal('0.00100020000')
data=str(data)
print(data.rstrip('0'))
# res = vformat(data)
# print(res)