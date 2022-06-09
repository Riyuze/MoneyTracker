from django.contrib import admin
from .models import Income, Source

# Register your models here.

class IncomeAdmin(admin.ModelAdmin):
    list_display = ('amount', 'description', 'source', 'date', 'user',)
    search_fields = ('description', 'source', 'date',)
    list_per_page = 5

admin.site.register(Income, IncomeAdmin)
admin.site.register(Source)