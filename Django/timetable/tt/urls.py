from django.urls import path
from . import views
urlpatterns = [
    path('', views.Inputform.as_view() )
    ]
