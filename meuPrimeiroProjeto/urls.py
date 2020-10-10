from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from clientes import urls as clients_urls

urlpatterns = [
                  path('person/', include(clients_urls)),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
