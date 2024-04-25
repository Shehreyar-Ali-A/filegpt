from django.urls import path
from .views import FileUploadView, HealthCheck

urlpatterns = [
    path('upload/', FileUploadView.as_view(), name='file-upload'),
    path('health-check/', HealthCheck.as_view(), name='health-check'),
]
