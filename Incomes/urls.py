from django.urls import path
from . import views

from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', views.index, name="incomes"),
    path('add-incomes', views.add_incomes, name="add-incomes"),
    path('edit-incomes/<int:id>', views.edit_incomes, name="edit-incomes"),
    path('delete-incomes/<int:id>', views.delete_incomes, name="delete-incomes"),
    path('search-incomes', csrf_exempt(views.search_incomes), name="search-incomes"),
    path("income-summary", views.income_summary, name="income-summary"),
    path('summary_rest', views.income_summary_rest, name='income_summary_rest'),
    path('three_months_summary', views.last_3months_income_stats, name='three_months_summary_'),
    path('last_3months_income_source_stats', views.last_3months_income_source_stats, name='last_3months_income_source_stats_'),
]
