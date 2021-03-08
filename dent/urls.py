from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from dent import settings

urlpatterns = [
    path('', include('main.urls')),
    path('', include('users.urls')),
    path('admin/', admin.site.urls),
    path('dashboard/', include('dashboard.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)