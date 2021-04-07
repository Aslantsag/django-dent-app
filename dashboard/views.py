from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, ListView, DeleteView, UpdateView
from django.views.generic.base import View, TemplateView

from dashboard.forms import MediaForm, PriceForm, InfoForm
from dent.lang_dict import lang_dict as l
from main.forms import NewLine
from main.models import Line
from mixin.permissions import UserIsOwnerMixin
from users.models import UserInfo, UserMedia, UserPrice


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "dashboard/index.html"


class LineListView(ListView):

    template_name = 'dashboard/line.html'
    context_object_name = 'line'

    def get_queryset(self):
        return Line.objects.filter(user=self.request.user, status='public')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = NewLine()
        return context


class PriceListView(ListView):

    template_name = 'dashboard/price_list.html'
    context_object_name = 'price_list'

    def get_queryset(self):
        return UserPrice.objects.filter(user=self.request.user, status='public')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = PriceForm()
        return context


class CreatePrice(LoginRequiredMixin, CreateView):

    def post(self, request):
        form = PriceForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.user_id = request.user.id
            item.save()
            messages.success(request, l['success_created'])
        return redirect('price_list')


class UpdatePrice(UserIsOwnerMixin, UpdateView):

    model = UserPrice
    form_class = PriceForm
    template_name = "dashboard/up_price_list.html"

    def post(self, request, pk):
        line = UserPrice.objects.get(pk=pk)
        form = PriceForm(request.POST, instance=line)
        if form.is_valid():
            form.save()
            messages.success(request, l['line_updated'])
        else:
            messages.error(request, l['invalid_err'])
        return redirect('price_list')


class DeletePrice(UserIsOwnerMixin, DeleteView):

    model = UserPrice

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        messages.success(request, l['success_deleted'])
        return redirect('price_list')


@login_required
def media(request):
    if request.method == 'POST':
        if 'submit' in request.POST:
            form = MediaForm(request.POST, request.FILES)
            if form.is_valid():
                item = form.save(commit=False)
                item.user = request.user
                item.save()
                messages.success(request, l['success_created'])
        else:
            pk = request.POST['pk']
            item = UserMedia.objects.get(pk=pk)
            if item.user_id == request.user.id:
                if 'edit' in request.POST:
                    form = MediaForm(instance=item)

                    data = {
                        'pk': pk,
                        'form': form
                    }
                    return render(request, "dashboard/up_media.html", data)

                if 'save' in request.POST:
                    form = MediaForm(request.POST, request.FILES, instance=item)
                    if form.is_valid():
                        form.save()
                        messages.success(request, l['success_updated'])

                if 'delete' in request.POST:
                    item.delete()
                    messages.success(request, l['success_deleted'])
            else:
                messages.error(request, l['permission_denied'])
        return redirect('media')
    else:
        form = MediaForm()
        item = UserMedia.objects.filter(user=request.user)

        data = {
            'form': form,
            'portfolio': item
        }
        return render(request, "dashboard/media.html", data)


@login_required
def contacts(request):
    if request.method == 'POST':
        if 'submit' in request.POST:
            form = InfoForm(request.POST, request.FILES)
            if form.is_valid():
                item = form.save(commit=False)
                item.user_id = request.user.id
                item.save()
                messages.success(request, l['success_created'])
            else:
                messages.error(request, form.errors)
        else:
            item = UserInfo.objects.get(user=request.user)
            if not item:
                return redirect('contacts')
            if 'edit' in request.POST:
                form = InfoForm(instance=item)

                data = {
                    'form': form
                }
                return render(request, "dashboard/up_contacts.html", data)

            if 'save' in request.POST:
                form = InfoForm(request.POST, request.FILES, instance=item)
                if form.is_valid():
                    form.save()
                    messages.success(request, l['success_updated'])

        return redirect('contacts')
    else:
        form = InfoForm()
        item = UserInfo.objects.filter(user=request.user).first()

        data = {
            'form': form,
            'user_info': item
        }
        return render(request, "dashboard/contacts.html", data)
