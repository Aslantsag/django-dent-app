from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from dent.lang_dict import lang_dict as l
from main.forms import NewLine
from main.models import Line
from users.models import UserPrice, UserInfo, UserMedia


def home(request):
    users = User.objects.filter(groups=1)
    data = {
        'title': l['site_title'],
        'users': users
    }
    return render(request, "main/home.html", data)


def line(request, pk):
    user = get_object_or_404(User, pk=pk)
    line = Line.objects.filter(user=user, status='public')

    data = {
        'title': 'Запись к стоматологу',
        'line': line,
        'user_id': user.id,
        'username': user.username
    }

    if request.user.is_authenticated and request.user.id == pk:
        data['form'] = NewLine()

    return render(request, "main/line.html", data)


def price_list(request, pk):
    user = get_object_or_404(User, id=pk)
    price_list = UserPrice.objects.filter(user=user)

    data = {
        'title': 'Прайс-Лист',
        'price_list': price_list,
        'user_id': user.id
    }
    return render(request, "main/price_list.html", data)


def media(request, pk):
    user = get_object_or_404(User, id=pk)
    portfolio = UserMedia.objects.filter(user=user)

    data = {
        'title': 'Портфолио',
        'portfolio': portfolio,
        'user_id': user.id
    }
    return render(request, "main/media.html", data)


def contacts(request, pk):
    user = get_object_or_404(User, id=pk)
    user_info = get_object_or_404(UserInfo, user=user)

    data = {
        'title': 'Контакты',
        'user_info': user_info,
        'user_id': user.id
    }
    return render(request, "main/contacts.html", data)

# class LineListView(ListView):
#     model = Line
#     context_object_name = "line"
#     template_name = "main/line.html"
#     queryset = model.objects.filter(status='public')
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         if self.request.user.is_authenticated:
#             context['form'] = NewLine()
#         return context