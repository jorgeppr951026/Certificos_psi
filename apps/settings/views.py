
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import View
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib.auth.mixins import LoginRequiredMixin


from .models import *
from .forms import *


class General(LoginRequiredMixin, UpdateView):
    model = Settings
    fields = ('__all__')
    template_name = 'settings/general-settings.html'
    #success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["segment"] = 'general-settings-company'
        return context


class UserBaseView(LoginRequiredMixin, View):
    model = CustomUser
    fields = ('username', 'first_name', 'last_name', 'email', 'permiss')
    success_url = reverse_lazy('users_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["segment"] = 'general-settings-users'
        return context

class UserListView(UserBaseView, ListView):
    template_name = 'settings/users/users_list.html'


class UserDetailView(UserBaseView, DetailView):
    template_name = 'settings/users/user_detail.html'


class UserCreateView(LoginRequiredMixin,CreateView):
    model = CustomUser
    form_class = UserCreationForm
    template_name = 'settings/users/user_create.html'
    success_url = reverse_lazy('users_list')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["segment"] = 'general-settings-users'
        return context


class UserUpdateView(LoginRequiredMixin ,UpdateView):
    model = CustomUser
    fields = ('first_name', 'last_name', 'email', 'permiss')
    template_name = 'settings/users/user_update.html'
    success_url = reverse_lazy('users_list')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["segment"] = 'general-settings-users'
        return context


class UserDeleteView(UserBaseView, DeleteView):
    template_name = 'settings/users/user_delete.html'
