
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Administrator/',include('Administrator.urls')),
    path('Basics/',include('Basics.urls')),
    path('',include('Guest.urls')),
    path('User/',include('User.urls')),
    path('Scrapcenter/',include('Scrapcenter.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)