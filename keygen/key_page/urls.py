from django.urls import path
from .views import *


urlpatterns = [
    path('generate/', SetSecretAPIView.as_view(), name='generate'),
    path('secrets/<slug:secret_key>', GetSecretAPIView.as_view(), name='secret')
]
