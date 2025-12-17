from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', include('students.urls')),
    path('api/', include('students.api_urls')),
    path('groups/', include('groups.urls')),
    path('courses/', include('courses.urls')),
    path('accounts/', include('django.contrib.auth.urls')),


]
