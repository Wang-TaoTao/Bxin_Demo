# -*- coding: utf-8 -*-
import requests
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings


def login_required(f):
    def _(request, *args, **kwargs):
        token = request.COOKIES.get('BX_PERMISSION_AUTH_TOKEN', '') or request.GET.get('token', '')
        if token:
            url = settings.BIXIN_PERMISSION_BASE_URL + '/http_rpc/user_info'
            params = {
                'access_token': settings.KARAZHAN_PERMISSION_ACCESS_TOKEN,
                'platform_flag': settings.KARAZHAN_PERMISSION_PLATFORM_FLAG,
                'jwt_token': token
            }
            resp = requests.get(url, params, timeout=15)
            if resp.status_code == 200:
                request.user_info = resp.json()
                permission_list = request.user_info.get('permission_list', [])
                request.perms = {k: 1 for k in permission_list}
                if request.GET.get('token'):
                    response = HttpResponseRedirect('https://{}{}'.format(request.get_host(), request.path))
                    response.set_cookie('BX_PERMISSION_AUTH_TOKEN', token)
                    return response
                return f(request, *args, **kwargs)
        current_url = 'https://{}{}'.format(request.get_host(), request.get_full_path())
        response = HttpResponseRedirect(settings.BIXIN_PERMISSION_BASE_URL + '/#/login?redirect={}&platform_flag={}'.format(current_url,
            settings.KARAZHAN_PERMISSION_PLATFORM_FLAG))
        response.set_cookie('BX_PERMISSION_AUTH_TOKEN', '')
        return response
    return _


def permission_required(permissions=''):
    def wrapper(func):
        @login_required
        def _(request, *args, **kwargs):
            if hasattr(request, 'user_info'):
                user_permission_list = request.user_info.get('permission_list', [])
                if user_permission_list:
                    if permissions:
                        if not isinstance(permissions, (list, tuple)):
                            permission_list = [permissions]
                        else:
                            permission_list = permissions
                        for p in permission_list:
                            if p in user_permission_list:
                                return func(request, *args, **kwargs)
                    else:
                        return func(request, *args, **kwargs)
            return HttpResponse('Forbidden', status=403)
        return _
    return wrapper
