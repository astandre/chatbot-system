from django.contrib import admin
from .models import *


# Register your models here.


class SocialNetworksAdmin(admin.ModelAdmin):
    list_display = ('id_account','user_name', 'social_network','user')
    list_filter = ['social_network']
    search_fields = ['user_name']


class InputsAdmin(admin.ModelAdmin):
    list_display = ('text', 'solved','created_at','social_network','intent')
    list_filter = ['solved']
    search_fields = ['text']


class UsersAdmin(admin.ModelAdmin):
    list_display = ('id_user','first_name', 'last_name', 'email')
    search_fields = ['first_name', 'last_name', 'email']


admin.site.register(SocialNetworks, SocialNetworksAdmin)
admin.site.register(Inputs, InputsAdmin)
admin.site.register(Users, UsersAdmin)
