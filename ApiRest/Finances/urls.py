from .views import ConfigFraisEleveViewset, PaiementFraisMensuelsViewset, PaiementAutresFraisViewset,\
    ConfigFraisInscriptionReinscriptionViewset, PaiementInscriptionReinscriptionViewset, EcolageEtAutresFraisViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'configFraisEleve', ConfigFraisEleveViewset, basename='configFraisEleve')
router.register(r'paiementFraisMensuels', PaiementFraisMensuelsViewset, basename='paiementFraisMensuels')
router.register(r'paiementAutresFrais', PaiementAutresFraisViewset, basename='paiementFraisMensuels')
router.register(r'ConfigFraisInscReinsc', ConfigFraisInscriptionReinscriptionViewset, basename='ConfigFraisInscReinsc')
router.register(r'PaiementInscriptionReinscription', PaiementInscriptionReinscriptionViewset, basename='PaiementInscReinsc')
router.register(r'ecolageAutresFrais', EcolageEtAutresFraisViewSet, basename='ecolageAutresFrais')
# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
