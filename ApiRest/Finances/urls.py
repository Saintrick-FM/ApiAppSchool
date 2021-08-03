from .views import ConfigFraisEleveViewset, PaiementFraisViewset, ConfigFraisInscriptionReinscriptionViewset, PaiementInscriptionReinscriptionViewset
from django.urls import path, include
from rest_framework.routers import DefaultRouter

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'configFraisEleve', ConfigFraisEleveViewset, basename='configFraisEleve')
router.register(r'paiementFraisEleve', PaiementFraisViewset, basename='paiementFrais')
router.register(r'ConfigFraisInscReinsc', ConfigFraisInscriptionReinscriptionViewset, basename='ConfigFraisInscReinsc')
router.register(r'PaiementInscriptionReinscription', PaiementInscriptionReinscriptionViewset, basename='PaiementInscReinsc')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
