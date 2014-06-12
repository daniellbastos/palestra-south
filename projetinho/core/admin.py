# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import *

class BaseAdmin(admin.ModelAdmin):
    pass

class ImagemAnexoAdmin(admin.TabularInline):
    extra = 1
    model = ImagemAnexo

class NoticiaAdmin(admin.ModelAdmin):
    inlines = [ImagemAnexoAdmin]

admin.site.register(Noticia, NoticiaAdmin)
admin.site.register(Autor, BaseAdmin)