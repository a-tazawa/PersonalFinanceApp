from django.shortcuts import render
from .models import Transaction

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
