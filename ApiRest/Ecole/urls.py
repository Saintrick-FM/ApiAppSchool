from rest_framework.routers import DefaultRouter
from django.urls import include, path
from .views import EcoleViewSet, SiteViewSet

routers = DefaultRouter()
routers.register(r'ecole', EcoleViewSet, basename='ecole')
routers.register(r'site', SiteViewSet, basename='site')


urlpatterns = [
    path('', include(routers.urls))
]
