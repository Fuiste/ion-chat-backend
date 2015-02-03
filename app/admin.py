from django.contrib import admin
from app.models import *
from custom_user.admin import EmailUserAdmin


__author__ = 'fuiste'


class MessageAdmin(admin.ModelAdmin):
    fields = ['text', 'created_at']


class ChatterAdmin(EmailUserAdmin):
    fieldsets = EmailUserAdmin.fieldsets + (
        (None, {'fields': ('is_admin',)}),
    )

    class Meta:
        verbose_name = 'Chat user'
        verbose_name_plural = 'Chat users'


admin.site.register(Chatter, ChatterAdmin)
admin.site.register(Message, MessageAdmin)