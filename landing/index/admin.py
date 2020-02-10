from django.contrib import admin

from landing.index import models


@admin.register(models.SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    pass


@admin.register(models.IndexPage)
class IndexPageAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ParsingCategories)
class ParsingCategoriesAdmin(admin.ModelAdmin):
    pass


@admin.register(models.FAQuestion)
class FAQuestionsAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Example)
class ExampleAdmin(admin.ModelAdmin):
    pass
