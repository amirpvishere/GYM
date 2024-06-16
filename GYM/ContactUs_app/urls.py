from django.urls import path
from . import views

urlpatterns = [
    path('item', views.item),
    path('', views.contact)
]
