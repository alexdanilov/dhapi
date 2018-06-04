from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from .views import RestaurantViewSet


router = DefaultRouter()
router.register(r'restaurants', RestaurantViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]
