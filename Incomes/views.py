from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Source, Income
from django.contrib import messages
from django.core.paginator import Paginator
import json
from UserPreferences.models import UserPreferences

# Create your views here.

def search_incomes(request):
    if request.method == 'POST':
        search_str = json.loads(request.body).get('searchText')

        incomes = Income.objects.filter(
            amount__istartswith=search_str, user=request.user) | Income.objects.filter(
            date__istartswith=search_str, user=request.user) | Income.objects.filter(
            description__icontains=search_str, user=request.user) | Income.objects.filter(
            source__icontains=search_str, user=request.user) 
            
        data = incomes.values()

        return JsonResponse(list(data), safe=False)

@login_required(login_url='authentication/login')

def index(request):
    income = Income.objects.filter(user=request.user)
    paginator = Paginator(income, 5)
    page_number = request.GET.get('page')
    page_obj = Paginator.get_page(paginator, page_number)
    currency = UserPreferences.objects.get(user=request.user).currency

    context = {
        'incomes': income,
        'page_obj': page_obj,
        'currency': currency,
    }

    return render(request, 'incomes/index.html', context)

def add_incomes(request):
    source = Source.objects.all()
    context = {
        'source': source,
        'values': request.POST
    }

    if request.method == 'GET':  
        return render(request, 'incomes/add_incomes.html', context)

    if request.method == 'POST':
        amount = request.POST['amount']
        description = request.POST['description']
        date = request.POST['income_date']
        source = request.POST['source']

        if not amount:
            messages.error(request, 'Amount is required')
            return render(request, 'incomes/add_incomes.html', context)

        if not description:
            messages.error(request, 'Description is required')
            return render(request, 'incomes/add_incomes.html', context)
    
        Income.objects.create(user=request.user, amount=amount, description=description, date=date, source=source)

        messages.success(request, 'Income saved successfully')

        return redirect('incomes')

def edit_incomes(request, id):
    income = Income.objects.get(pk=id)
    source = Source.objects.all()
    context = {
        'income': income,
        'values': income,
        'source': source,
    }

    if request.method == 'GET':
        return render(request, 'incomes/edit_incomes.html', context)

    if request.method == 'POST':
        amount = request.POST['amount']
        description = request.POST['description']
        date = request.POST['income_date']
        source = request.POST['source']

        if not amount:
            messages.error(request, 'Amount is required')
            return render(request, 'incomes/edit_incomes.html', context)

        if not description:
            messages.error(request, 'Description is required')
            return render(request, 'incomes/edit_incomes.html', context)

        income.user = request.user
        income.amount = amount
        income.description = description
        income.date = date
        income.source = source

        income.save()

        messages.success(request, 'Income updated successfully')

        return redirect('incomes')

def delete_incomes(request, id):
    income = Income.objects.get(pk=id)
    income.delete()

    messages.success(request, 'Income deleted')

    return redirect('incomes')