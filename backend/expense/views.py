from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy

from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView
)

from .models import Expense
from .forms import ExpenseForm


def expense_list(request):
    template_name = 'expense/expense_list.html'

    object_list = Expense.objects.all()

    context = {
        'object_list': object_list,
    }
    return render(request, template_name, context)


class ExpenseListView(ListView):
    template_name = 'expense/expense.html'
    model = Expense
    context_object_name = 'expenses'
    paginate_by = 3


def expense_detail(request, pk):
    template_name = 'expense/expense_detail.html'
    # instance = Expense.objects.get(pk=pk)
    instance = get_object_or_404(Expense, pk=pk)

    context = {
        'object': instance,
    }
    return render(request, template_name, context)


class ExpenseDetailView(DetailView):
    model = Expense


def expense_create(request):
    template_name = 'expense/expense_form.html'
    form = ExpenseForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('expense:expense_list')

        return redirect('expense:expense_create')

    context = {
        'form': form
    }
    return render(request, template_name, context)


class ExpenseCreateView(CreateView):
    model = Expense
    form_class = ExpenseForm
    success_url = reverse_lazy('expense:expense_list')


def expense_update(request, pk):
    template_name = 'expense/expense_form.html'
    instance = get_object_or_404(Expense, pk=pk)
    form = ExpenseForm(request.POST or None, request.FILES, instance=instance)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('expense:expense_list')

    context = {
        'object': instance,
        'form': form,
    }
    return render(request, template_name, context)


class ExpenseUpdateView(UpdateView):
    model = Expense
    form_class = ExpenseForm


def expense_delete(request, pk):
    instance = get_object_or_404(Expense, pk=pk)
    instance.delete()
    print('Deletado com sucesso.')
    return redirect('expense:expense_list')
