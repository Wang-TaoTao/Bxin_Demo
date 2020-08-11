# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig


class KarazhanConfig(AppConfig):
    name = 'karazhan'

    # Django启动时自动扫描所有app下面的karazhan模块
    def ready(self):
        from django.utils.module_loading import autodiscover_modules
        autodiscover_modules('karazhan_config')
        # FIXME
        autodiscover_modules('karazhan_config_tars')
