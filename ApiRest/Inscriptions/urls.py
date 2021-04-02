from ApiRest.Inscriptions import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'inscriptions', views.EleveViewset, basename='eleve')


# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
