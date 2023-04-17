from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('11/api-cart/admin/', admin.site.urls),
    path('11/api-cart/', include('api.urls')),
]
