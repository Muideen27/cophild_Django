# urls.py
from django.urls import include, path
from rest_framework import routers
from .views import SailorViewSet, ProfileViewSet, PostViewSet

router = routers.DefaultRouter()
router.register(r'sailors', SailorViewSet)
router.register(r'profiles', ProfileViewSet)
router.register(r'posts', PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

