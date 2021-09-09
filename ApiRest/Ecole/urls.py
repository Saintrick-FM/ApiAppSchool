from rest_framework.routers import DefaultRouter
from django.urls import include, path

from .views import EcoleViewSet,CycleViewSet ,SiteViewSet, ClasseViewSet, EnseignantViewSet, MatiereViewSet,  AnneeScolaireViewSet


routers = DefaultRouter()
routers.register(r'matiere', MatiereViewSet, basename='matiere')
routers.register(r'ecole', EcoleViewSet, basename='ecole')
routers.register(r'site', SiteViewSet, basename='site')
routers.register(r'classe', ClasseViewSet, basename='classe')
routers.register(r'cycle', CycleViewSet, basename='cycle')
routers.register(r'enseignants', EnseignantViewSet, basename='enseignants')

routers.register(r'anneeScolaire', AnneeScolaireViewSet, basename='anneeScolaire')

urlpatterns = [
path('', include(routers.urls))

]
"""

urlpatterns += [
path('photos/', PhotoView),
path('matiere/', MatiereList.as_view()),
path('matiere/<int:pk>/', MatiereDetail.as_view()),
]

#urlpatterns = format_suffix_patterns(urlpatterns)
"""