from django.contrib import admin
from main.models import Line
from users.models import UserPrice, UserInfo, UserMedia

admin.site.register(Line)
admin.site.register(UserPrice)
admin.site.register(UserInfo)
admin.site.register(UserMedia)
