"""valoresDeMiPeru URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from experience.urls import experiences_patterns

urlpatterns = [

    # Path core
    path('', include('core.urls')),

    path('admin/', admin.site.urls),

    # Path de contact
    path('contact/', include('contact.urls')),

    # Path de experiencie
    path('experience/', include(experiences_patterns)),

    # paths de promotion
    path('promotion/', include('promotion.urls', namespace='promotion')),

    # Path de autenticacion
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('registration.urls')),
]

if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)