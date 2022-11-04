from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ArtisteViewSet,SongViewSet,LyricViewSet


router = DefaultRouter()
router.register(r'artiste', ArtisteViewSet, basename='artiste')
router.register(r'song', SongViewSet, basename='song')
router.register(r'lyric', LyricViewSet, basename='lyric')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = []+router.urls