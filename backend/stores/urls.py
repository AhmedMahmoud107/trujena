from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from rest_framework.routers import DefaultRouter , SimpleRouter
from rest_framework_nested.routers import NestedDefaultRouter


router = SimpleRouter()

router = SimpleRouter()
router.register(r'stores', views.StoreList, basename='store')
router.register(r'sections', views.SectionList, basename='section')
router.register(r'templates', views.SectionTemplates, basename='template')

urlpatterns = router.urls + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
