from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from django.views.generic.base import TemplateView

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
        else:
            messages.error(request, l['invalid_err'])
        return redirect('price_list')


class UpdatePrice(UserIsOwnerMixin, UpdateView):

    model = UserPrice
    form_class = PriceForm
    template_name = "dashboard/up_price_list.html"

    def post(self, request, pk):
        data = UserPrice.objects.get(pk=pk)
        form = PriceForm(request.POST, instance=data)
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


class MediaListView(ListView):

    template_name = 'dashboard/media.html'
    context_object_name = 'portfolio'

    def get_queryset(self):
        return UserMedia.objects.filter(user=self.request.user, status='public')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = MediaForm()
        return context


class CreateMedia(LoginRequiredMixin, CreateView):

    def post(self, request):
        form = MediaForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.user_id = request.user.id
            item.save()
            messages.success(request, l['success_created'])
        else:
            messages.error(request, form.errors)
        return redirect('media')


class UpdateMedia(UserIsOwnerMixin, UpdateView):

    model = UserMedia
    form_class = MediaForm
    template_name = "dashboard/up_media.html"

    def post(self, request, pk):
        data = self.model.objects.get(pk=pk)
        form = self.form_class(request.POST, instance=data)
        if form.is_valid():
            form.save()
            messages.success(request, l['success_updated'])
        else:
            messages.error(request, l['invalid_err'])
        return redirect('media')


class DeleteMedia(UserIsOwnerMixin, DeleteView):

    model = UserMedia

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        messages.success(request, l['success_deleted'])
        return redirect('media')


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
