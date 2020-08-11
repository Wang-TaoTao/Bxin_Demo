import datetime
import csv
import pytz
import math
import decimal
from decimal import Decimal

from django.conf import settings
from django.http import JsonResponse, HttpResponse
from django.db.models.query import QuerySet


d0 = Decimal('0')
ADMIN_TZ = getattr(settings, 'ADMIN_TZ', 'Asia/Shanghai')


def get_paginator_info(page, datas, per_page=50, item_count=None):
    if not item_count:
        if isinstance(datas, QuerySet):
            item_count = datas.count()
        else:
            item_count = len(datas)
    pages_count = math.ceil(item_count/per_page)
    if pages_count <= 11 or page <= 6:  # case 1 and 2
        pages = [x for x in range(1, min(pages_count + 1, 12))]
    elif page > pages_count - 6:  # case 4
        pages = [x for x in range(pages_count - 10, pages_count + 1)]
    else:  # case 3
        pages = [x for x in range(page - 5, page + 6)]
    if page < pages_count - 5:
        show_last_page_num = True
    else:
        show_last_page_num = False
    return {
        'current_page': page,
        'show_pages': pages,
        'item_count': item_count,
        'last_page': pages_count,
        'show_last_page_num': show_last_page_num,
    }


def ok_json(**kw):
    kw['ok'] = True
    return JsonResponse(kw)


def error_json(error, status=200):
    resp = {'ok': False,
            'error': error}
    res = JsonResponse(resp, status=status)
    res.messenger_ok = False
    return res


def format_csv_items(items):
    results = []
    for item in items:
        if isinstance(item, (int, float, Decimal)):
            item = vformat(item, 6)
        elif isinstance(item, datetime.datetime):
            item = item.strftime('%Y-%m-%d')

        results.append(item)
    return results


def export_csv(titles, contents, filename):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=%s' % filename
    writer = csv.writer(response)
    writer.writerow(titles)
    for line in contents:
        writer.writerow(line)
    return response


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


def str_2_bj(s, format_str="%Y-%m-%d %H:%M:%S"):
    tz = pytz.timezone(ADMIN_TZ)
    d = datetime.datetime.strptime(s, format_str)
    return tz.localize(d)


def utc_2_bj_str(d, format_str="%Y-%m-%d %H:%M:%S"):
    return (d + datetime.timedelta(hours=8)).strftime(format_str)


def get_operator(request):
    name = request.user_info.get('name', '')
    id = request.user_info.get('id', '')
    return '{}({})'.format(name, id)


def normalize_datetime(value, tz_name=None):
    if not value.tzinfo:
        value = value.replace(tzinfo=pytz.timezone(settings.TIME_ZONE))
    if not tz_name:
        tz_name = ADMIN_TZ
    tz = pytz.timezone(tz_name)
    return tz.normalize(value)


def parse_decimal(v, digits=8, default=d0):
    try:
        return floor_decimal(Decimal(v), digits=digits)
    except decimal.InvalidOperation:
        return default


def floor_decimal(amount, digits=8):
    return amount.quantize(
        Decimal('1E-%d' % digits),
        context=decimal.Context(rounding=decimal.ROUND_FLOOR)
    )
