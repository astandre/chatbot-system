from django.contrib import admin
from .models import *


# Register your models here.


class QuestionsInline(admin.TabularInline):
    model = Questions
    extra = 5


class SlotsInline(admin.TabularInline):
    model = Slots
    extra = 1


class QuestionsAdmin(admin.ModelAdmin):
    inlines = [SlotsInline]
    list_display = ('question', 'intent')
    list_filter = ['intent']
    search_fields = ['question']


class IntentsAdmin(admin.ModelAdmin):
    inlines = [QuestionsInline]
    list_display = ('name', 'description', 'answer')
    search_fields = ['name']


class SynonymsInline(admin.TabularInline):
    model = Synonyms
    extra = 5


class ValuesInline(admin.TabularInline):
    model = Values
    extra = 1


class EntitiesInline(admin.TabularInline):
    model = Entities
    extra = 1


class EntitiesAdmin(admin.ModelAdmin):
    inlines = [ValuesInline]
    list_display = ('entity', 'type', 'synonyms', 'extensible')
    list_filter = ['type', 'synonyms', 'extensible']
    search_fields = ['entity']


class SlotsAdmin(admin.ModelAdmin):
    list_display = ('slot_name', 'question', 'entity')
    list_filter = ['entity']
    search_fields = ['slot_name']


class ValuesAdmin(admin.ModelAdmin):
    inlines = [SynonymsInline]
    list_display = ('value', 'entity')
    list_filter = ['entity']
    search_fields = ['value']


class SynonymsAdmin(admin.ModelAdmin):
    list_display = ('synonym', 'value')
    list_filter = ['value']
    search_fields = ['synonym']


class IntentCheckAdmin(admin.ModelAdmin):
    list_display = ('clear_question', 'intent', 'entity')
    list_filter = ['intent','entity']
    search_fields = ['clear_question']


admin.site.register(Intents, IntentsAdmin)
admin.site.register(Questions, QuestionsAdmin)
admin.site.register(Entities, EntitiesAdmin)
admin.site.register(Values, ValuesAdmin)
admin.site.register(Synonyms, SynonymsAdmin)
admin.site.register(Slots, SlotsAdmin)
admin.site.register(IntentCheck, IntentCheckAdmin)
