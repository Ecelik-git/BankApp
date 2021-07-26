from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView
from . import views

urlpatterns = [
    path('', views.home, name='bank-home'),
    #path('customer/<int:pk>/', PostDetailView.as_view(), name='bank-customer_page'),#to see each customer
    #path('customer/', PostListView.as_view(), name='bank-customer_page'),
    #path('customer/<int:pk>/', PostCreateView.as_view(), name='customer-create'),
    path('view/', views.view, name='bank-customer_page'),
    path('customer/<int:pk>/update/', PostUpdateView.as_view(), name='customer-update'),
    path('about/', views.about, name='bank-about'),
]