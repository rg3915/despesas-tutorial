from django.urls import path

from backend.expense import views as v

app_name = 'expense'

urlpatterns = [
    path('', v.ExpenseListView.as_view(), name='expense_list'),
    path('create/', v.ExpenseCreateView.as_view(), name='expense_create'),
    path('<int:pk>/', v.ExpenseDetailView.as_view(), name='expense_detail'),
    path('<int:pk>/update/', v.expense_update, name='expense_update'),
    path('<int:pk>/delete/', v.expense_delete, name='expense_delete'),
]
