from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Category, Expense
from django.contrib import messages

# Create your views here.

@login_required(login_url='authentication/login')

def index(request):
    expenses = Expense.objects.filter(user=request.user)

    context = {
        'expenses': expenses,
    }

    return render(request, 'expenses/index.html', context)

def add_expenses(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
        'values': request.POST
    }

    if request.method == 'GET':  
        return render(request, 'expenses/add_expenses.html', context)

    if request.method == 'POST':
        amount = request.POST['amount']
        description = request.POST['description']
        date = request.POST['expense_date']
        category = request.POST['category']

        if not amount:
            messages.error(request, 'Amount is required')
            return render(request, 'expenses/add_expenses.html', context)

        if not description:
            messages.error(request, 'Description is required')
            return render(request, 'expenses/add_expenses.html', context)
    
        Expense.objects.create(user=request.user, amount=amount, description=description, date=date, category=category)

        messages.success(request, 'Expense saved successfully')

        return redirect('expenses')
