from django.urls import path, include
from rest_framework import routers
from .views import (UserViewSet, CityListAPIView, CityDetailAPIView, PropertyListAPIView, PropertyDetailAPIView,
                    PropertyImageListAPIView, PropertyImageDetailAPIView, BookingListAPIView, BookingDetailAPIView,
                    ReviewDetailAPIView, ReviewListAPIView, AmenityViewSet, RegisterView, CustomLoginView,
                    LogoutView, BookingViewSet, ReviewCreateAPIView, PropertyCreateAPIView)

router = routers.SimpleRouter()
router.register(r'users', UserViewSet)
router.register('booking', BookingViewSet)
router.register(r'amenity', AmenityViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register_list'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('city/', CityListAPIView.as_view(), name='city-list'),
    path('city/<int:pk>/', CityDetailAPIView.as_view(), name='city-detail'),
    path('property/', PropertyListAPIView.as_view(), name='property-list'),
    path('property/<int:pk>/', PropertyDetailAPIView.as_view(), name='property-detail'),
    path('property/create/', PropertyCreateAPIView.as_view(), name='property-create'),
    path('property_image/', PropertyImageListAPIView.as_view(), name='property-image'),
    path('property_image/<int:pk>/', PropertyImageDetailAPIView.as_view(), name='property-detail'),
    path('booking/', BookingListAPIView.as_view(), name='booking-list'),
    path('booking/<int:pk>/', BookingDetailAPIView.as_view(), name='detail'),
    path('review/', ReviewListAPIView.as_view(), name='review-list'),
    path('review/<int:pk>/', ReviewDetailAPIView.as_view(), name='review-detail'),
    path('review/create/', ReviewCreateAPIView.as_view(), name='review-create'),
]