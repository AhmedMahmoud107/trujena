from rest_framework import viewsets, mixins
from .models import Store, Section, Template
from .serializers import SectionSerializer , StoreSerializer, SectionTemplatesSerializer

from rest_framework import viewsets, mixins
from .models import Store, Section, Template
from .serializers import SectionSerializer, StoreSerializer, SectionTemplatesSerializer


class AuthantecatiedStoreOwner:
    def filter_queryset_by_user(self, queryset, user='user'):
        return queryset.filter(**{f"{user}": self.request.user})


class StoreList(viewsets.ReadOnlyModelViewSet, AuthantecatiedStoreOwner):
    serializer_class = StoreSerializer
    def get_queryset(self):
        queryset =Store.objects.all()
        return self.filter_queryset_by_user(queryset, user='user')


class SectionList(viewsets.ReadOnlyModelViewSet, AuthantecatiedStoreOwner):
    serializer_class = SectionSerializer

    def get_queryset(self):
        store_pk = self.kwargs.get('store_pk')
        queryset = Section.objects.filter(store_id=store_pk)
        return self.filter_queryset_by_user(queryset, user='store_id__user')


class SectionTemplates(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    AuthantecatiedStoreOwner
    ):
    serializer_class = SectionTemplatesSerializer

    def get_queryset(self):
        section_pk = self.kwargs.get('section_pk')
        queryset =Template.objects.filter(section_id=section_pk)
        return self.filter_queryset_by_user(queryset, user='section_id__store_id__user')