from rest_framework.routers import DefaultRouter
from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import EcoleViewSet, SiteViewSet, ClasseViewSet, EnseignantViewSet, PhotoView, MatiereList, MatiereDetail

routers = DefaultRouter()
# routers.register(r'matiere', MatiereViewSet, basename='matiere')
routers.register(r'ecole', EcoleViewSet, basename='ecole')
routers.register(r'site', SiteViewSet, basename='site')
routers.register(r'classe', ClasseViewSet, basename='classe')
routers.register(r'enseignants', EnseignantViewSet, basename='enseignants')


urlpatterns = [
    path('photos', PhotoView),
    path('matiere/', MatiereList.as_view()),
    path('matiere/<int:pk>/', MatiereDetail.as_view()),
    #path('', include(routers.urls)),
]
urlpatterns = format_suffix_patterns(urlpatterns)
