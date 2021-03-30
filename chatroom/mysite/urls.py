from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views
from django.conf.urls import url
from django.conf.urls import include

urlpatterns = [
    path('adminadminadmin/', admin.site.urls),
    path('', include('page.urls')),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(next_page='/'), name='logout'),
    url(r'^api-auth/', include('rest_framework.urls')),
    path('social-auth/', include('social_django.urls', namespace="social")),  
]

