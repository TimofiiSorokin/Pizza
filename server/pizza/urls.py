from django.conf.urls import include
from django.contrib import admin
from django.urls import path

api_urlpatterns = [
    path('', include(('company.api.urls', 'company'), namespace='company')),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('api/', include((api_urlpatterns, 'company'), namespace='api')),
]
