from os import stat
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
# from courses.views import Course

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.authtoken')),
    
    path('api/courses/', include("courses.urls")),
    path('api/users/', include("users.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
