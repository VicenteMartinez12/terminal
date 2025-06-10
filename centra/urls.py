from django.contrib import admin
from django.urls import path
from centra.views import menu_principal

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', menu_principal, name='menu_principal'),
]
