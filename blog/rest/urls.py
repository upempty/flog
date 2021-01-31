from django.urls import path
from rest.views import FirstView

urlpatterns = [
    path('', FirstView.as_view()),
]