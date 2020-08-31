from rest_framework.generics import ListAPIView, GenericAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from company.api.serializers import CatalogListSerializer
from company.api.pagination import NoLimitPagination
from company.models import Catalog


class HomePageAPIView(ListAPIView):
    pagination_class = NoLimitPagination
    serializer_class = CatalogListSerializer
    queryset = Catalog.objects.all()
    permission_classes = (AllowAny, )
