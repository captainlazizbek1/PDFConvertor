from django.urls import path
from convertor.views import ConvertorView

urlpatterns = [
    path('convert/', ConvertorView.as_view())
]