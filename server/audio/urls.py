from .views import audio_upload
from django.urls import path

urlpatterns = [
    path('', audio_upload)
]
