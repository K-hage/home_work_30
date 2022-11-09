from rest_framework.viewsets import ModelViewSet

from ads.models import Category
from ads.serializers import CategorySerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.order_by('name').all()
    serializer_class = CategorySerializer
