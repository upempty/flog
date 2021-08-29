from django.urls import path
from rest.views import FirstView
from rest.views import DecorationCartView
from rest.views import ArticleView
from rest.views import ArticleAPIView
from rest.views import LoginView

urlpatterns = [
    path('', FirstView.as_view()),
    path('cart/', DecorationCartView.as_view()),
    path('article/', ArticleAPIView.as_view()),
    #path('article/', ArticleView.as_view()),
    path('login/', LoginView.as_view()),
]
