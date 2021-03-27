from django.urls import include, path
from .views import ClassViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'classe', ClassViewset)

urlpatterns = [
    path('', include(router.urls))
]
