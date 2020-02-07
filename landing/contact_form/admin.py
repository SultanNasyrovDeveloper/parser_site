from django.contrib import admin

from landing.contact_form import models


@admin.register(models.ContactForm)
class ContactFormAdmin(admin.ModelAdmin):
    pass
