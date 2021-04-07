from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, CreateView, UpdateView
from dent.lang_dict import lang_dict as l
from main.forms import NewLine, RegisterForm
from main.models import Line
from mixin.permissions import UserIsOwnerMixin


def back_url(request):
    # return f'/line/{request.user.id}'
    return request.META.get('HTTP_REFERER', '/')


class AddLine(LoginRequiredMixin, CreateView):
    def post(self, request):
        form = NewLine(request.POST)
        user = get_object_or_404(User, pk=request.user.id)
        form.user = user
        if form.is_valid():
            line = form.save(commit=False)
            line.user = user
            line.save()
            messages.success(request, l['line_created'])
        else:
            messages.error(request, l['invalid_err'])
        return redirect(back_url(request))


class UpdateLine(UserIsOwnerMixin, UpdateView):
    model = Line
    form_class = NewLine
    # template_name = "users/line_update.html"
    template_name = "dashboard/up_line.html"

    def post(self, request, pk):
        line = Line.objects.get(pk=pk)
        form = NewLine(request.POST, instance=line)
        if form.is_valid():
            form.save()
            messages.success(request, l['line_updated'])
        else:
            messages.error(request, l['invalid_err'])
        return redirect(back_url(request))


class DeleteLine(UserIsOwnerMixin, DeleteView):
    model = Line

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = back_url(request)
        self.object.delete()
        messages.success(request, l['line_deleted'])
        return redirect(success_url)


class SignUpView(SuccessMessageMixin, CreateView):
    template_name = 'registration/sign_up.html'
    success_url = reverse_lazy('login')
    form_class = RegisterForm
    success_message = l['sign_up_success']

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        return super(SignUpView, self).get(request, *args, **kwargs)



