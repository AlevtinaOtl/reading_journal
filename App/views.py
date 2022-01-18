from django.shortcuts import render, redirect
from .models import Book
from django.views.generic.base import View
from django.views import generic
from django.views.generic.edit import UpdateView, CreateView, DeleteView, FormView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


class CustomLoginView(LoginView):
    template_name = 'login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    success_url = reverse_lazy('home')

    def get_success_url(self):
        return reverse_lazy('home')


class RegisterPage(FormView):
    template_name = 'register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')
        return super(RegisterPage, self).get(*args, **kwargs)


class BookList(LoginRequiredMixin, View):
    model = Book

    def get(self, request):
        books = Book.objects.all().filter(user=self.request.user)
        amount = Book.objects.all().filter(user=self.request.user).count()
        return render(request, 'book_list.html', {
            'book_list': books,
            'amount': amount
        })


class DetailView(LoginRequiredMixin, generic.DetailView):
    model = Book
    template_name = 'book_detail.html'


class AddBook(LoginRequiredMixin, CreateView):
    model = Book
    fields = ['title', 'author', 'year', 'description', 'review']
    success_url = reverse_lazy('home')
    template_name = 'add_book.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddBook, self).form_valid(form)


class EditBook(LoginRequiredMixin, UpdateView):
    model = Book
    fields = ['title', 'author', 'year', 'description', 'review']
    success_url = reverse_lazy('home')
    template_name = 'add_book.html'


class DeleteBook(LoginRequiredMixin, DeleteView):
    model = Book
    success_url = reverse_lazy('home')
    template_name = 'task_confirm_delete.html'
