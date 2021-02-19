from django.urls import path
from rest.views import FirstView
from rest.views import DecorationCartView

urlpatterns = [
    path('', FirstView.as_view()),
    path('cart/', DecorationCartView.as_view()),
]
