"""home_work_30 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from ads import views
from ads.views.ad import AdViewSet
from ads.views.category import CategoryViewSet
from ads.views.selection import SelectionViewSet
from home_work_30 import settings
from users.views.location import LocationViewSet

router = routers.SimpleRouter()
router.register(r'cat', CategoryViewSet)
router.register(r'location', LocationViewSet)
router.register(r'ad', AdViewSet)
router.register(r'selection', SelectionViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.root),
    path('', include(router.urls)),
    path('ad/', include('ads.urls.ad')),
    path('user/', include('users.urls.user')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
