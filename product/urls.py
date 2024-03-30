from django.urls import path
from . import views

urlpatterns = [
    path('', views.product, name='product'),
    path('<int:pk>/', views.product_detail, name='product_detail'),
    path('store',views.store.as_view(),name='store'),
    path('store/<int:pk>/',views.store_detail.as_view(),name='store_detail'),
    path('review',views.ReviewList.as_view(),name='review_list'),
    path('review/<int:pk>',views.ReviewDetail.as_view(),name='review_detail'),



]