from django.urls import path
from . import views

urlpatterns = [
        path('sailors', views.sailors, name='sailors'),
]
