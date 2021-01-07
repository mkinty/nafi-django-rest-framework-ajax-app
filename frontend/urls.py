from django.urls import path
from frontend import views

app_name = 'frontend'

urlpatterns = [
    # post views
    path('', views.index, name='list'),
]