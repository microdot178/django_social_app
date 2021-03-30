from django.urls import path
from . import views
from page.views import *
from django.conf.urls import url
from django.conf.urls import include

urlpatterns = [
    #path('', views.page, name='page'),
    path('', views.message, name='message'),
    path('accounts/profile/', views.REDIRECT, name='REDIRECT'),
    url(r'^api-auth/', include('rest_framework.urls')),
    url('messages/', PageSerializerView.as_view()),
]