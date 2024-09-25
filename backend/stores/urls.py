from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedDefaultRouter


router = DefaultRouter()
router.register(r'stores', views.StoreList, basename='store')

stores_router = NestedDefaultRouter(router, r'stores', lookup='store')
stores_router.register(r'sections', views.SectionList, basename='store-sections')

sections_router = NestedDefaultRouter(stores_router, r'sections', lookup='section')
sections_router.register(r'templates', views.SectionTemplates, basename='section-templates')


urlpatterns = router.urls + stores_router.urls + sections_router.urls + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns = [
#     router.urls + stores_router.urls,
    
#     path('<int:store_pk>/sections', views.SectionList.as_view()),
#     path('section/<int:section_pk>/templates', views.SectionTemplatesList.as_view()),
#     path('section/<int:section_pk>/templates/<int:template_pk>', views.SectionTemplatesRetrive.as_view()),
# ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# router = DefaultRouter()
# router.register(r'stores', StoreViewSet, basename='store')

# # إنشاء الراوتر المتداخل للأقسام داخل المتاجر
# stores_router = NestedDefaultRouter(router, r'stores', lookup='store')
# stores_router.register(r'sections', SectionViewSet, basename='store-sections')

# # جمع كل الراوترات معًا
# urlpatterns = router.urls + stores_router.urls