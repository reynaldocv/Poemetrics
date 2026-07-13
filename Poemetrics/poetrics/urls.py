from django.urls import path
from . import views

urlpatterns = [
    path('/', views.webpage, name='webpage'),
    path('analysis/', views.analysis, name='analysis'),
    path('test/', views.test, name='test'),
]


