from django.urls import path
from . import views

urlpatterns = [
    path('board/', views.board, name='quiz-board'),
    path('<str:key>/', views.submit, name='quiz-home'),
]
