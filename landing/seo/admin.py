from django.contrib import admin

from landing.seo import models


@admin.register(models.PageSeo)
class PageSeoAdmin(admin.ModelAdmin):
    pass


@admin.register(models.PostSeo)
class PostSeoAdmin(admin.ModelAdmin):
    pass