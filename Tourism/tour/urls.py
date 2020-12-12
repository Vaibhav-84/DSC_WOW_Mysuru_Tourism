from django.urls import path
from .views import homepage
from . import views

urlpatterns = [
    path('', homepage, name='index'),
    path('Zoo/', views.Zoo, name='tour'),
    path('Palace/', views.Palace, name='tour'),
    path('Hills/', views.Hills, name='tour'),
    path('Gardens/', views.Gardens, name='tour'),
    path('feedback/', views.feedback, name='tour'),
    path('volunteer/', views.volunteer, name='tour'),
]