
from django.contrib import admin
from django.urls import path, include
from boda_app.views import home


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('boda_app.urls') )
]
