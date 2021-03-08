from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.generic import ListView, DeleteView
from django.views.generic.base import View

from dent.lang_dict import lang_dict as l
from main.forms import NewLine, RegisterForm
from main.models import Line


class AddLine(View):
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
        return redirect(f'/line/{request.user.id}')


# class UpdateLine(View):
#     templete_name = ""
#
#     def post(self, request, pk):
#         line = Line.objects.get(pk=pk)
#         form = NewLine(request.POST, instance=line)
#         if form.is_valid():
#             form.save()
#             messages.success(request, l['line_updated'])
#         else:
#             messages.error(request, l['invalid_err'])
#         return redirect(back_url(request))


@login_required
def update_line(request, pk):
    line = Line.objects.get(id=pk)

    form = NewLine(instance=line)

    if request.method == 'POST':
        if line.user_id == request.user.id:
            form = NewLine(request.POST, instance=line)
            if form.is_valid():
                form.save()
                return redirect(back_url(request))
        else:
            messages.error(request, l['permission_denied'])
    context = {
        'form': form,
        'user_id': request.user.id,
    }

    return render(request, 'users/line_update.html', context)


@login_required
def delete_line(request, pk):
    line = Line.objects.get(pk=pk)
    if line.user_id == request.user.id:
        try:
            line.delete()
            messages.success(request, l['line_deleted'])
        except:
            messages.error(request, l['db_err'])
    else:
        messages.error(request, l['permission_denied'])
    return redirect(back_url(request))


def sign_up(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, l['sign_up_success'])
            return redirect('login')
    else:
        form = RegisterForm()

    data = {
        'form': form
    }
    return render(request, "registration/sign_up.html", data)


# def login(request):
#
#     if not request.user.is_authenticated:
#
#         if request.method == 'POST':
#             form = RegisterForm(request.POST)
#             if form.is_valid():
#                 form.save()
#                 return redirect('/line/')
#     else:
#         return redirect('/')
#
#     data = {
#         'form': form,
#     }
#     return render(request, "main/login.html", data)


def back_url(request):
    return f'/line/{request.user.id}'
