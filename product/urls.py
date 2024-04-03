from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register('store',views.Store_Viewset, basename="store")

urlpatterns = [
    path('', views.product, name='product'),
    path('<int:pk>/', views.product_detail, name='product_detail'),
    path('',include(router.urls)),
    # path('store',views.store.as_view(),name='store'),
    # path('store/<int:pk>/',views.store_detail.as_view(),name='store_detail'),
    # path('review',views.ReviewList.as_view(),name='review_list'),
    # path('review/<int:pk>',views.ReviewDetail.as_view(),name='review_detail'),
    path('store/<int:pk>/review-create',views.ReviewCreate.as_view(),name='review_create'),
    path('store/<int:pk>/review',views.ReviewList.as_view(),name="review_list"),
    path('store/review/<int:pk>',views.ReviewDetail.as_view(),name='review_detail'),

    



]