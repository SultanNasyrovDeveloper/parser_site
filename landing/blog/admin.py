from django.contrib import admin

from landing.blog import models


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    pass
