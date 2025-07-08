from django.shortcuts import render, redirect
from .models import Transaction
from .forms import TransactionForm

def root_redirect(request):
    return redirect('login')

def transaction_list(request):
    transactions = Transaction.objects.filter(user=request.user).order_by('date')  # 昇順に並べ替え
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
            transaction.user = request.user  # ユーザーを設定
            transaction.save()
            return redirect('transaction_list')
    else:
        form = TransactionForm()

    return render(request, 'finance_tracker/add_transaction.html', {'form': form})
