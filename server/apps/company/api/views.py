from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView, GenericAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from company.api.serializers import CatalogListSerializer, CatalogDetailSerializer
from company.api.pagination import NoLimitPagination
from company.models import Catalog


class CatalogPageAPIView(ListAPIView):
    pagination_class = NoLimitPagination
    serializer_class = CatalogListSerializer
    queryset = Catalog.objects.all()
    permission_classes = (AllowAny, )


class CatalogCreateAPIView(CreateAPIView):
    serializer_class = CatalogDetailSerializer


class CatalogDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CatalogDetailSerializer
    queryset = Catalog.objects.all()


