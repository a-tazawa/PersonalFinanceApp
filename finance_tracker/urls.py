from django.urls import path
from . import views

urlpatterns = [
    path('', views.root_redirect, name='root_redirect'),
    path('transactions/', views.transaction_list, name='transaction_list'),
    path('transactions/add/', views.add_transaction, name='add_transaction'),
    path('transactions/<int:pk>/edit/', views.edit_transaction, name='edit_transaction'),
    path('transaction/<int:pk>/delete/', views.delete_transaction, name='delete_transaction'),
]
