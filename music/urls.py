from django.urls import path, include

from rest_framework.authtoken import views
from .views import ActorViewSet,MovieViewSet
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('actors', ActorViewSet,basename='actors')
router.register('movies', MovieViewSet,basename='movies')




urlpatterns = [
    path('',include(router.urls)),


]

