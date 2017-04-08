from django.conf.urls import url
from .viewset import BoardgameViewSet
from rest_framework.routers import DefaultRouter

''' Register the Django rest framework viewset to be able to be used as URLs '''
router = DefaultRouter()
router.register(r'boardgames', BoardgameViewSet, base_name='boardgames')
urlpatterns = router.urls
