from django.urls import include, path, re_path
from django.views.generic import TemplateView
from rest_framework import routers
from .views import SailorViewSet, ProfileViewSet, PostViewSet

router = routers.DefaultRouter()
router.register(r'sailors', SailorViewSet)
router.register(r'profiles', ProfileViewSet)
router.register(r'posts', PostViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    re_path(r'^.*$', TemplateView.as_view(template_name='index.html')),  # Catch-all route
]
