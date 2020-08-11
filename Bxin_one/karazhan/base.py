# -*- coding: utf-8 -*-
import sys
import time
import pytz
from operator import methodcaller

from datetime import datetime
from decimal import Decimal

from django.conf.urls import url
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from karazhan.helpers import get_paginator_info, ok_json, error_json, \
    export_csv, format_csv_items, vformat, str_2_bj, utc_2_bj_str, get_operator
from karazhan.decorators import permission_required, login_required


class KarazhanConfig(object):
    # 要在列表里展示的列
    list_display = []
    # 筛选器
    filter_fields = []
    # 排序列
    sort_fields = []
    # 默认排序列
    default_sort_name = ''
    # 默认排序方向
    default_sort_order = 'desc'
    # 每页展示条数
    per_page = 20
    # ModelForm
    form_class = None
    # verbose_name以及自定义字段
    field_verbose_name_mapping = {}
    # 创建者字段
    creator_field = None
    # 操作者字段
    operator_field = None
    # 基础权限（如果没有配读权限，写权限，导出权限的话，会用基础权限自动生成, 规则为 BASE_PERM + ''/'_WRITE'/'_EXPORT'）
    base_perm = ''
    # 读权限
    read_perms = []
    # 写权限
    write_perms = []
    # 导出权限
    export_perms = []
    # 是否可以删除
    can_delete = False
    # 自定义按钮
    button_config = []
    # 字段返回None时展示什么
    none_field_default_show = '-'
    '''
    {
        'url': 'https://www.baidu.com/s?wd={xxx},  # xxx为字段对应的值，会调用format方法给它赋值
        'name': '打开百度搜索',
        'target': '_blank',  # 默认_self, 对应html <a>表桥的target
        'type': 'normal',  # normal / javascript, 默认normal
    }
    如果type为javascript, 会调用js的post，此时请将参数放在url的params中，系统会自动将其转为data发送，返回结果请调用error_json / ok_json
    '''

    def __init__(self, model_class, config_class):
        self.model_class = model_class
        self.config_class = config_class

    @property
    def urls(self):
        partterns = [
            url(r'^$', self.list_view),
            url(r'^add/', self.add_view),
            url(r'^(\d+)/change/$', self.edit_view),
            url(r'^(\d+)/delete/$', self.delete_view),

        ]

        return partterns

    # 自定义queryset
    def get_queryset(self):
        return self.model_class.objects.order_by('-id')

    # 展示列表
    @method_decorator(login_required)
    def list_view(self, request):
        read_perms = self.read_perms or self.base_perm and [self.base_perm]
        write_perms = self.write_perms or self.base_perm and ['{}_WRITE'.format(self.base_perm)]
        export_perms = self.export_perms or self.base_perm and ['{}_EXPORT'.format(self.base_perm)]
        is_has_permissions = self.is_has_permissions(request.user_info, read_perms)
        if not is_has_permissions:
            return HttpResponse('Forbidden', status=403)
        page = int(request.GET.get('page', 1))
        sort_name = sort = request.GET.get('sort_name') or self.get_default_sort_name()
        sort_order = request.GET.get('sort_order', self.default_sort_order or 'desc')

        filter_info = self.init_filter_field()
        queryset = self.get_queryset()

        filter_result = self.get_filter_result(request, filter_info, queryset)
        filter_data = filter_result.get('filter_data')
        queryset = filter_result.get('queryset')

        list_display = self.resolve_list_display()

        is_export = request.GET.get('is_export_csv', False)
        if is_export and self.is_has_permissions(request.user_info, export_perms):
            return self._export(list_display, queryset)

        is_custom_table_export = request.GET.get('is_export_custom_table_csv', False)
        if is_custom_table_export and self.is_has_permissions(request.user_info, export_perms):
            return self._export_custom_table()

        if sort_name and sort_order:
            queryset = self.sort_data(sort_name, sort_order, queryset)
        else:
            queryset = queryset.all()
        data_list = []
        datas = queryset[self.per_page * (page - 1): self.per_page * page]
        for row in datas:
            button_config_list = []
            data = self.resolve_row(row)
            data_dict = dict(zip(self.list_display, data['datas']))
            for bc in self.button_config:
                button_config_list.append({
                    'url': bc['url'].format(**data_dict),
                    'name': bc['name'],
                    'target': bc.get('target', '_self'),
                    'type': bc.get('type', 'normal')
                })
            data['button_config_list'] = button_config_list
            data_list.append(data)

        item_count = queryset.count()
        paginator_info = get_paginator_info(page, data_list, per_page=self.per_page, item_count=item_count)
        list_display_sort_info = [bool(l in self.sort_fields) for l in self.list_display]

        try:
            custom_table_data = self.get_custom_table_data(request)
        except NotImplementedError as e:
            custom_table_data = None

        params = {
            'data_list': data_list,
            'sort_name': sort_name,
            'sort_order': sort_order,
            'list_display': zip(self.list_display, list_display, list_display_sort_info),
            'paginator_info': paginator_info,
            'filter_data': filter_data,
            'filter_info': filter_info,
            'is_readonly': not (bool(self.form_class) and self.is_has_permissions(request.user_info, write_perms)),
            'form': self.form_class and self.form_class() or '',
            'is_can_export': self.is_has_permissions(request.user_info, export_perms),
            'is_can_delete': self.can_delete,
            'custom_table_data': custom_table_data,  # 自定义table
        }
        return render(request, 'list.html', params)

    # 添加
    @csrf_exempt
    @method_decorator(login_required)
    def add_view(self, request):
        write_perms = self.write_perms or self.base_perm and ['{}_WRITE'.format(self.base_perm)]
        is_has_permissions = self.is_has_permissions(request.user_info, write_perms)
        if not is_has_permissions:
            return HttpResponse('Forbidden', status=403)
        if request.method == 'POST':
            form = self.form_class(request.POST, request.FILES)
            if form.is_valid():
                new_obj = form.save(commit=False)
                if self.creator_field:
                    new_obj.__dict__[self.creator_field] = get_operator(request)
                if self.operator_field:
                    new_obj.__dict__[self.operator_field] = get_operator(request)
                new_obj.save()
                form.save_m2m()
                try:
                    self.add_hook(request, new_obj)
                except NotImplementedError as e:
                    pass
                return ok_json()
            else:
                return error_json(form.errors)
        else:
            return error_json('method need post')

    # 编辑
    @csrf_exempt
    @method_decorator(login_required)
    def edit_view(self, request, object_id):
        write_perms = self.write_perms or self.base_perm and ['{}_WRITE'.format(self.base_perm)]
        is_has_permissions = self.is_has_permissions(request.user_info, write_perms)
        if not is_has_permissions:
            return HttpResponse('Forbidden', status=403)
        try:
            obj = self.model_class.objects.get(id=object_id)
        except Exception as e:
            return error_json('object not found')

        form = self.form_class(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            obj = form.save(commit=False)
            form.save_m2m()
            if self.operator_field:
                obj.__dict__[self.operator_field] = get_operator(request)
            obj.save()
            try:
                self.edit_hook(request, obj)
            except NotImplementedError as e:
                pass
            return ok_json()
        else:
            return error_json(form.errors)

    # 删除
    @csrf_exempt
    @method_decorator(login_required)
    def delete_view(self, request, object_id):
        if not self.can_delete:
            return error_json('can not delete')

        write_perms = self.write_perms or self.base_perm and ['{}_WRITE'.format(self.base_perm)]
        is_has_permissions = self.is_has_permissions(request.user_info, write_perms)
        if not is_has_permissions:
            return HttpResponse('Forbidden', status=403)
        try:
            obj = self.model_class.objects.get(id=object_id)
        except Exception as e:
            return error_json('object not found')

        try:
            data = self.delete(obj)
            try:
                self.delete_hook(request, object_id)
            except NotImplementedError as e:
                pass
            return ok_json()
        except NotImplementedError as e:
            if obj.delete():
                return ok_json()
            return error_json('delete failed')
        except Exception as e:
            return error_json(str(e))

    # 自定义删除方法, 例如软删除
    def delete(self, obj):
        raise NotImplementedError


    # 初始化过滤字段
    def init_filter_field(self):
        filter_info = []
        for field in self.filter_fields:
            filter_func = getattr(self, '{}_filter_info'.format(field), None)
            if filter_func:
                filter_info.append(filter_func())
            else:
                _type = self.model_class._meta.get_field(field).get_internal_type()
                title = self.resolve_field_display(field)
                if _type == 'DateTimeField':
                    filter_info.append({
                        'field': field,
                        'title': title,
                        'type': 'datetime_range_filter',
                        'start_time': u'起始时间',
                        'end_time': u'结束时间',
                    })

                if _type == 'CharField' or _type == 'ForeignKey' or _type == 'IntegerField':
                    filter_info.append({
                        'field': field,
                        'title': title,
                        'type': 'search_filter',
                    })

        return filter_info

    # 获取过滤数据
    def get_filter_result(self, request, filter_info, queryset):
        filter_data = {}
        for _filter in filter_info:
            if _filter['type'] == 'datetime_range_filter':
                start_time = request.GET.get('{}_start_time'.format(_filter['field']))
                if start_time:
                    start_time = str_2_bj(start_time, '%Y-%m-%d %H:%M:%S')
                    filter_dict = {'{}__gte'.format(_filter['field']): start_time}
                    queryset = queryset.filter(**filter_dict)
                    filter_data['{}_start_time'.format(_filter['field'])] = start_time
                end_time = request.GET.get('{}_end_time'.format(_filter['field']))
                if end_time:
                    end_time = str_2_bj(end_time, '%Y-%m-%d %H:%M:%S')
                    filter_dict = {'{}__lt'.format(_filter['field']): end_time}
                    queryset = queryset.filter(**filter_dict)
                    filter_data['{}_end_time'.format(_filter['field'])] = end_time
            if _filter['type'] == 'select_filter' or _filter['type'] == 'search_filter':
                select_option = request.GET.get(_filter['field'])
                if select_option:
                    try:
                        queryset = methodcaller('resolve_%s_filter' % _filter['field'], \
                                                queryset, select_option)(self)
                    except AttributeError:
                        filter_dict = {_filter['field']: select_option}
                        queryset = queryset.filter(**filter_dict)
                    filter_data[_filter['field']] = select_option
        return {'filter_data': filter_data, 'queryset': queryset}

    # 获取展示字段
    def resolve_list_display(self):
        list_display = []
        for c in self.list_display:
            title = self.resolve_field_display(c)
            list_display.append(title)
        return list_display

    def resolve_field_display(self, field):
        try:
            title = methodcaller('kc_%s' % field)(self)
        except AttributeError:
            title = self.field_verbose_name_mapping.get(field)
        if not title:
            title = self.model_class._meta.get_field(field).verbose_name
        return title

    # 获取行数据
    def resolve_row(self, row):
        data = []
        for column in self.list_display:
            if column.startswith('kc_'):
                resolve_func = getattr(self, 'resolve_{}'.format(column), '')
                value = resolve_func and resolve_func(row) or ''
            else:
                try:
                    value = methodcaller('resolve_%s' % column, row)(self)
                except AttributeError:
                    value = getattr(row, column)
            value = self.format_column_value(value)
            data.append(value)
        return {
            'id': bool(self.form_class) and row.id or None,
            'form': self.form_class and self.form_class(instance=row) or '',
            'datas': data
        }

    # 格式化列值
    def format_column_value(self, value):
        if value is None:
            return self.none_field_default_show
        elif isinstance(value, (int, float, Decimal)):
            return vformat(value)
        elif isinstance(value, datetime):
            return utc_2_bj_str(value)
        elif isinstance(value, list):
            return '\n'.join(value)
        elif sys.version_info[0] < 3 and isinstance(value, unicode):
            return value.encode('utf-8')
        return value

    # 检查权限
    def is_has_permissions(self, user, permissions):
        if not permissions:
            return True
        user_permission_list = user.get('permission_list', [])
        if user_permission_list:
            if not isinstance(permissions, (list, tuple)):
                permission_list = [permissions]
            else:
                permission_list = permissions
            for p in permission_list:
                if p in user_permission_list:
                    return True
        return False

    # 导出
    def _export(self, list_display, queryset):
        titles = [title for title in list_display]
        titles = format_csv_items(titles)
        contents = [format_csv_items(self.resolve_row(data).get('datas')) \
                    for data in queryset]
        return export_csv(titles, contents, \
                          '%s_%s.csv' % (self.model_class._meta.model_name, int(time.time())))

    # 导出自定义table
    def _export_custom_table(self):
        data = self.get_custom_table_data()
        titles = format_csv_items(data['head'])
        contents = [format_csv_items(row) for row in data['body']]
        return export_csv(titles, contents, \
                          '%s_%s.csv' % (self.model_class._meta.model_name, int(time.time())))

    # 排序
    def sort_data(self, sort_name, sort_order, queryset):
        # 暂时仅支持原生字段排序，后续会支持自定义字段排序
        if sort_name in self.list_display and not sort_name.startswith('kc_'):
            _sort_name = sort_order == 'desc' and sort_name or '-{}'.format(sort_name)
            return queryset.order_by(_sort_name)
        # reverse = sort_order == 'desc'
        # datas = sorted(datas.values(), key=lambda x: x.get(sort_name), reverse=reverse)

    def get_default_sort_name(self):
        if self.sort_fields and self.default_sort_name:
            return self.default_sort_name
        if self.sort_fields:
            return self.sort_fields[0]
        return ''

    # 自定义table
    def get_custom_table_data(self, request=None):
        '''
        return {
            'is_can_export': '',
            'title': 'sss',
            'head': ['a', 'b', 'c'],
            'body': [
                ['a1', 'b1', 'c1'],
                ['a2', 'b2', 'c2']
            ]
        }
        '''
        raise NotImplementedError

    def add_hook(self, request, obj):
        raise NotImplementedError

    def edit_hook(self, request, obj):
        raise NotImplementedError

    def delete_hook(self, request, obj):
        raise NotImplementedError


class KarazhanSiteRegister(object):

    def __init__(self):
        # 存放models url views 对应关系
        self._registry = {}
        self._json_registry = []

    def register(self, class_name, config_class, sub_path=''):
        self._registry[class_name] = (config_class(class_name, self), sub_path)

    def register_json(self, config_class, path):
        self._json_registry.append((config_class(), path))

    @property
    def urls(self):
        partterns = []
        for model_class, _karazhan_config_obj in self._registry.items():
            karazhan_config_obj = _karazhan_config_obj[0]
            sub_path = _karazhan_config_obj[1]
            if sub_path:
                app_model_name_urls = r'^{0}/{1}/'.format(model_class._meta.app_label, sub_path)
            else:
                app_model_name_urls = r'^{0}/{1}/'.format(model_class._meta.app_label, model_class._meta.model_name)
            _partterns = url(app_model_name_urls, (karazhan_config_obj.urls, None, None))
            partterns.append(_partterns)

        for karazhan_config_obj, path in self._json_registry:
            urls = r'^{}/'.format(path)
            _partterns = url(urls, (karazhan_config_obj.urls, None, None))
            partterns.append(_partterns)

        return partterns, None, None


site = KarazhanSiteRegister()
