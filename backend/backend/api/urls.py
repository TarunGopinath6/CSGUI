
from django.urls import path, include
from .views import (
    SampleApiView,
)

urlpatterns = [
    path('sample', SampleApiView.as_view()),
]