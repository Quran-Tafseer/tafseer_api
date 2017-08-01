# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Sura, Ayah


class SuraAdmin(admin.ModelAdmin):
    list_display = ('index', 'name')


class AyahAdmin(admin.ModelAdmin):
    list_display = ('sura', 'number', 'text')


admin.site.register(Sura, SuraAdmin)
admin.site.register(Ayah, AyahAdmin)
