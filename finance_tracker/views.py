from django.shortcuts import render, redirect, get_object_or_404
from .models import Transaction
from .forms import TransactionForm

def root_redirect(request):
    return redirect('login')

def transaction_list(request):
    transactions = Transaction.objects.filter(user=request.user).order_by('date')
    balance = 0
    transaction_with_balance = []

    for t in transactions:
        if t.type == 'income':
            income = t.amount
            expense = 0
        else:
            income = 0
            expense = t.amount
        balance += income - expense
        transaction_with_balance.append({
            'id': t.id,
            'date': t.date,
            'category': t.category,
            'description': t.description,
            'type': t.type,
            'amount': t.amount,
            'income': income,
            'expense': expense,
            'balance': balance,
        })

    return render(request, 'finance_tracker/transaction_list.html', {
        'transactions': transaction_with_balance
    })

def add_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user
            transaction.save()
            return redirect('transaction_list')
    else:
        form = TransactionForm()

    return render(request, 'finance_tracker/add_transaction.html', {'form': form})

def edit_transaction(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    if request.method == 'POST':
        form = TransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
            return redirect('transaction_list')
    else:
        form = TransactionForm(instance=transaction)
    return render(request, 'finance_tracker/edit_transaction.html', {'form': form})

from django.shortcuts import render, redirect, get_object_or_404

def delete_transaction(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    if request.method == 'POST':
        transaction.delete()
        return redirect('transaction_list')
    return render(request, 'finance_tracker/delete_transaction_confirm.html', {'transaction': transaction})

