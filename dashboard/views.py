from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from dashboard.forms import MediaForm, PriceForm, InfoForm
from dent.lang_dict import lang_dict as l
from main.forms import NewLine
from main.models import Line
from users.models import UserInfo, UserMedia, UserPrice

@login_required
def index(request):
    return render(request, "dashboard/index.html")

@login_required
def line(request):
    if request.method == 'POST':
        if 'submit' in request.POST:
            form = NewLine(request.POST)
            if form.is_valid():
                item = form.save(commit=False)
                item.user_id = request.user.id
                item.save()
                messages.success(request, l['success_created'])
        else:
            pk = request.POST['pk']
            item = Line.objects.get(pk=pk)
            if item.user == request.user:
                if 'edit' in request.POST:
                    form = NewLine(instance=item)

                    data = {
                        'pk': pk,
                        'form': form
                    }
                    return render(request, "dashboard/up_line.html", data)

                if 'save' in request.POST:
                    form = NewLine(request.POST, request.FILES, instance=item)
                    if form.is_valid():
                        form.save()
                        messages.success(request, l['success_updated'])

                if 'delete' in request.POST:
                    item.delete()
                    messages.success(request, l['success_deleted'])
            else:
                messages.error(request, l['permission_denied'])
        return redirect('line')
    else:
        form = NewLine()
        item = Line.objects.filter(user=request.user)

        data = {
            'form': form,
            'line': item
        }
        return render(request, "dashboard/line.html", data)

@login_required
def price_list(request):
    if request.method == 'POST':
        if 'submit' in request.POST:
            form = PriceForm(request.POST)
            if form.is_valid():
                item = form.save(commit=False)
                item.user_id = request.user.id
                item.save()
                messages.success(request, l['success_created'])
        else:
            pk = request.POST['pk']
            item = UserPrice.objects.get(pk=pk)
            if item.user == request.user:
                if 'edit' in request.POST:
                    form = PriceForm(instance=item)

                    data = {
                        'pk': pk,
                        'form': form
                    }
                    return render(request, "dashboard/up_price_list.html", data)

                if 'save' in request.POST:
                    form = PriceForm(request.POST, request.FILES, instance=item)
                    if form.is_valid():
                        form.save()
                        messages.success(request, l['success_updated'])

                if 'delete' in request.POST:
                    item.delete()
                    messages.success(request, l['success_deleted'])
            else:
                messages.error(request, l['permission_denied'])
        return redirect('price_list')
    else:
        form = PriceForm()
        item = UserPrice.objects.filter(user=request.user)

        data = {
            'form': form,
            'price_list': item
        }
        return render(request, "dashboard/price_list.html", data)

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
