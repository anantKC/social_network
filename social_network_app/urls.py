"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .register import RegisterView

urlpatterns = [
    path('', include('social_network_core_app.urls')),
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='social_network_core_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='social_network_core_app:home')),
    path('register/', RegisterView.as_view(), name='register'),
    path('', include('django.contrib.auth.urls'))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
