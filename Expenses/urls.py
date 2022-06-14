from django.urls import path
from . import views

from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', views.index, name="expenses"),
    path('add-expenses', views.add_expenses, name="add-expenses"),
    path('edit-expenses/<int:id>', views.edit_expenses, name="edit-expenses"),
    path('delete-expenses/<int:id>', views.delete_expenses, name="delete-expenses"),
    path('search-expenses', csrf_exempt(views.search_expenses), name="search-expenses"),
    path("expense-summary", views.expense_summary, name="expense-summary"),
    path('summary_rest', views.expense_summary_rest, name='expenses_summary_rest'),
    path('three_months_summary', views.last_3months_stats, name='three_months_summary'),
    path('last_3months_expense_source_stats', views.last_3months_expense_source_stats, name="last_3months_expense_source_stats"),
    path('export-csv', views.export_csv, name="export-csv"),
]
