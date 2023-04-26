from django.urls import path
from .views import login_view, data_upload_view


urlpatterns = [
path('login/', login_view, name='login'),
path('upload/', data_upload_view, name='upload'),
]