from rest_framework.routers import DefaultRouter
from django.urls import include, path
from .views import EcoleViewSet, SiteViewSet, ClasseViewSet, EnseignantViewSet, MatiereViewSet

routers = DefaultRouter()
routers.register(r'ecole', EcoleViewSet, basename='ecole')
routers.register(r'site', SiteViewSet, basename='site')
routers.register(r'classe', ClasseViewSet, basename='classe')
routers.register(r'enseignants', EnseignantViewSet, basename='enseignants')
routers.register(r'matiere', MatiereViewSet, basename='matiere')


urlpatterns = [
    path('', include(routers.urls))
]
