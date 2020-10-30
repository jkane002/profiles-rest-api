from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profiles_api import views

# Generate different routes for our viewset
router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
router.register('profile', views.UserProfileViewSet) # doesn't need base name bc of query set

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('', include(router.urls))
]
