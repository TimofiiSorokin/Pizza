from rest_framework import serializers

from company.models import Catalog


class CatalogListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catalog
        fields = '__all__'


class CatalogDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catalog
        fields = '__all__'

