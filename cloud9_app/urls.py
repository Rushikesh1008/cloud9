from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('form_submit', views.form_submit,name="form_submit"),
]

