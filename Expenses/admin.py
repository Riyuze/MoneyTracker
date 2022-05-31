from sre_constants import CATEGORY_DIGIT
from django.contrib import admin
from .models import  Expense, Category

# Register your models here.

admin.site.register(Expense)
admin.site.register(Category)