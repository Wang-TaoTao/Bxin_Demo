from decimal import Decimal

from django import template
from django.conf import settings

from karazhan.helpers import normalize_datetime, parse_decimal


DEFAULT_CURRENCY = getattr(settings, 'DEFAULT_CURRENCY', 'bitcoin')

register = template.Library()


@register.filter(name='formatuser')
def formatuser(value):
    return '{}({})'.format(value.nickname, value.name)


@register.filter(name='get_dict_value')
def get_dict_value(obj, key):
    if key in obj:
        return obj[key]
    return


@register.filter(name='percent')
def percent(value):
    if not value:
        return 0
    return Decimal(str(value)) * Decimal(100)


@register.filter(name='hdatetime')
def hdatetime(value, request=None):
    if not value:
        return ''
    tz_name = request and request.COOKIES.get('timezone') or None
    value = normalize_datetime(value, tz_name=tz_name)
    return value.strftime("%Y-%m-%d %H:%M:%S")


@register.filter(name='hdate')
def hdate(value, request=None):
    tz_name = request and request.COOKIES.get('timezone') or None
    value = normalize_datetime(value, tz_name=tz_name)
    return value.strftime("%Y-%m-%d")


@register.filter(name='dformat')
def dformat(value, currency='BTC'):
    if isinstance(value, str) or value is None:
        value = parse_decimal(v=value)

    if currency in ('BTC',):
        hold_len = 8
        fmt = '%i.%08i'
        k = 100000000
    else:
        hold_len = 2
        fmt = '%i.%02i'
        k = 100

    sign = ''
    if value < 0:
        value = -value
        sign = '-'

    upv = value * (10 ** hold_len)

    r = fmt % (upv // k, upv % k)
    r = sign + r.rstrip('0').rstrip('.')
    if r == '-0':
        r = '0'
    return r
