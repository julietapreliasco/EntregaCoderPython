from django.urls import path
from .views import inicio, un_template

urlpatterns = [
    path('', inicio),
    path('mi-template', un_template)
]