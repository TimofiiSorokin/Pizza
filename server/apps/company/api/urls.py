from django.urls import path

from company.api.views import (HomePageAPIView, )

urlpatterns = [
    path('home-page', HomePageAPIView.as_view(), name='home-page'),
]