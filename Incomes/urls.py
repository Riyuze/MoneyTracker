from django.urls import path
from . import views

from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', views.index, name="incomes"),
    path('add-incomes', views.add_incomes, name="add-incomes"),
    path('edit-incomes/<int:id>', views.edit_incomes, name="edit-incomes"),
    path('delete-incomes/<int:id>', views.delete_incomes, name="delete-incomes"),
    path('search-incomes', csrf_exempt(views.search_incomes), name="search-incomes"),
]
