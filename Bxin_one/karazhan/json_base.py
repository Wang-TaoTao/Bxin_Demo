import uuid

from django.conf.urls import url
from django.shortcuts import render

from karazhan.helpers import get_paginator_info


class KarazhanJsonConfig(object):

    list_display = []
    filter_fields = []
    per_page = 20
    list_display_show_mapping = {}

    @property
    def urls(self):
        partterns = [
            url(r'^$', self.list_view),
        ]

        return partterns

    def get_data_head(self):
        return [self.list_display_show_mapping.get(i, '') for i  in self.list_display]

    def get_data_list(self):
        return []

    def list_view(self, request):
        page = int(request.GET.get('page', 1))

        filter_info = self.init_filter_field()

        _data_list = self.get_data_list()
        filter_data = self.get_filter_result(request, filter_info)
        paginator_info = get_paginator_info(page, _data_list, per_page=self.per_page, item_count=len(_data_list))
        _data_list = _data_list[self.per_page * (page - 1): self.per_page * page]
        data_list = []
        for data in _data_list:
            row_data = []
            if filter_data:
                if all([data.get(_filter) == _value for _filter, _value in filter_data.items()]):
                    data_list.append([data.get(i) for i in self.list_display])
            else:
                data_list.append([data.get(i) for i in self.list_display])

        params = {
            'data_head': self.get_data_head(),
            'data_list': data_list,
            'filter_info': filter_info,
            'filter_data': filter_data,
            'paginator_info': paginator_info
        }
        return render(request, 'json_list.html', params)

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
    def get_filter_result(self, request, filter_info):
        filter_data = {}
        for _filter in filter_info:
            if _filter['type'] == 'select_filter' or _filter['type'] == 'search_filter':
                select_option = request.GET.get(_filter['field'])
                if select_option:
                    filter_data[_filter['field']] = select_option
        return filter_data
