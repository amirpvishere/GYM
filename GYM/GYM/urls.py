from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home),
    path("contact/", include("ContactUs_app.urls")),
    path("trainer/", include("trainer.urls")),
    path("why", views.why),
    path("home", views.home),
]
