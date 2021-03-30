from django.contrib import admin
from django.urls import path,include
from .views import FilterView
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
from django.http import HttpResponse


def okay(request):
    return HttpResponse('pretend-binary-data-here', content_type='image/jpeg')
urlpatterns = [
    # path('filter/', FilterView.as_view()),
    path('', FilterView.as_view()),
    path('favicon.ico', okay),
    
]