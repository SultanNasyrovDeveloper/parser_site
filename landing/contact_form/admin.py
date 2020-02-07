from django.contrib import admin

from landing.contact_form import models


@admin.register(models.ContactForm)
class ContactFormAdmin(admin.ModelAdmin):
    fields = ('name', 'phone_number', 'message')
    readonly_fields = ('created', )
