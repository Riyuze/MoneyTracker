from sre_constants import CATEGORY_DIGIT
from django.contrib import admin
from .models import  Expense, Category

# Register your models here.

class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('amount', 'description', 'category', 'date', 'user',)
    search_fields = ('description', 'category', 'date',)
    list_per_page = 5

admin.site.register(Expense, ExpenseAdmin)
admin.site.register(Category)