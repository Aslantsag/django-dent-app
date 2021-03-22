from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.views.generic import View, ListView, DetailView
from dent.lang_dict import lang_dict as l
from main.forms import NewLine
from main.models import Line
from users.models import UserPrice, UserInfo, UserMedia


class HomeView(ListView):

    queryset = User.objects.filter(groups=1)
    template_name = 'main/home.html'
    context_object_name = 'users'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = l['home_page_title']
        return context


class LineListView(ListView):

    template_name = 'main/line.html'
    context_object_name = 'line'

    def get_queryset(self):
        user = get_object_or_404(User, pk=self.kwargs['pk'])
        queryset = Line.objects.filter(user=user, status='public')
        return queryset

    def get_context_data(self, **kwargs):
        pk = self.kwargs['pk']
        user = get_object_or_404(User, pk=pk)
        context = super().get_context_data(**kwargs)
        context['title'] = l['line_page_title']
        context['user_id'] = user.id
        context['username'] = user.username
        if self.request.user.is_authenticated and self.request.user.id == pk:
            context['form'] = NewLine()
        return context


class PriceView(ListView):

    template_name = 'main/price_list.html'
    context_object_name = 'price_list'

    def get_queryset(self):
        user = get_object_or_404(User, pk=self.kwargs['pk'])
        queryset = UserPrice.objects.filter(user=user)
        return queryset

    def get_context_data(self, **kwargs):
        pk = self.kwargs['pk']
        user = get_object_or_404(User, pk=pk)
        context = super().get_context_data(**kwargs)
        context['title'] = l['price_page_title']
        context['user_id'] = user.id
        return context


class MediaView(ListView):

    template_name = 'main/media.html'
    context_object_name = 'portfolio'

    def get_queryset(self):
        user = get_object_or_404(User, pk=self.kwargs['pk'])
        queryset = UserMedia.objects.filter(user=user)
        return queryset

    def get_context_data(self, **kwargs):
        pk = self.kwargs['pk']
        user = get_object_or_404(User, pk=pk)
        context = super().get_context_data(**kwargs)
        context['title'] = l['price_page_title']
        context['user_id'] = user.id
        return context


class ContactView(ListView):

    template_name = 'main/contacts.html'
    context_object_name = 'user_info'

    def get_queryset(self):
        user = get_object_or_404(User, pk=self.kwargs['pk'])
        return get_object_or_404(UserInfo, user=user)

    def get_context_data(self, **kwargs):
        pk = self.kwargs['pk']
        user = get_object_or_404(User, pk=pk)
        context = super().get_context_data(**kwargs)
        context['title'] = l['contact_page_title']
        context['user_id'] = user.id
        return context