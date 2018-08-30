from django.contrib import admin
from .models import *


# Register your models here.


class SocialNetworksAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'social_network')
    list_filter = ['social_network','user__first_name']
    search_fields = ['user_name']


class InputsAdmin(admin.ModelAdmin):
    list_display = ('text', 'solved')
    list_filter = ['solved']
    search_fields = ['text']


class UsersAdmin(admin.ModelAdmin):
    list_display = ('id_number', 'first_name', 'last_name')
    search_fields = ['id_number', 'id_oc', 'first_name', 'last_name']


admin.site.register(SocialNetworks, SocialNetworksAdmin)
admin.site.register(Inputs, InputsAdmin)
admin.site.register(Users, UsersAdmin)
