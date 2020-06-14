from django.urls import path
from.views import (
ReviewListView,
ReviewDetailView,
ReviewCreateView,
ReviewUpdateView,
ReviewDeleteView,
DogListView,
BunnyListView,
CatListView)
from . import views

urlpatterns = [
    path('', views.home, name = 'pawpals-home'),
    path('dogs/', views.dogs, name = 'pawpals-dogs'),
    path('cats/', views.cats, name = 'pawpals-cats'),
    path('bunnies/', views.bunnies, name = 'pawpals-bunnies'),
    path('reviews/', ReviewListView.as_view(), name = 'pawpals-reviews'),
    path('reviews/<int:pk>/', ReviewDetailView.as_view(), name = 'review-detail'),
    path('reviews/<int:pk>/update/', ReviewUpdateView.as_view(), name = 'review-update'),
    path('reviews/<int:pk>/delete/', ReviewDeleteView.as_view(), name = 'review-delete'),
    path('reviews/new/', ReviewCreateView.as_view(), name = 'review-create'),
    path('dogs/', DogListView.as_view(), name = 'pawpals-dogs'),
    path('bunnies/', BunnyListView.as_view(), name = 'pawpals-bunnies'),
    path('cats/', CatListView.as_view(), name = 'pawpals-cats')
]
