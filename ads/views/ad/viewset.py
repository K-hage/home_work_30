from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import ModelViewSet

from ads.models import Ad
from ads.permissions import IsOwnerAdOrStaff
from ads.serializers import AdSerializer, AdDetailSerializer, AdListSerializer


class AdViewSet(ModelViewSet):
    queryset = Ad.objects.select_related('author', 'category').order_by('-price').all()

    default_serializer = AdSerializer
    serializer_classes = {
        'retrieve': AdDetailSerializer,
        'list': AdListSerializer,
    }

    default_permission = [AllowAny()]
    permissions = {
        'retrieve': [IsAuthenticated()],
        'destroy': [IsAuthenticated(), IsOwnerAdOrStaff()],
        'update': [IsAuthenticated(), IsOwnerAdOrStaff()],
        'partial-update': [IsAuthenticated(), IsOwnerAdOrStaff()],
    }

    def get_permissions(self):
        return self.permissions.get(self.action, self.default_permission)

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer)

    def list(self, request, *args, **kwargs):
        categories = request.GET.getlist('cat', [])
        if categories:
            self.queryset = self.queryset.filter(category_id__in=categories)

        text = request.GET.get('text')
        if text:
            self.queryset = self.queryset.filter(name__icontains=text)

        location = request.GET.get('location')
        if location:
            self.queryset = self.queryset.filter(author__location__name__icontains=location)

        price_from = request.GET.get('price_from')
        price_to = request.GET.get('price_to')
        if price_to:
            self.queryset = self.queryset.filter(price__lte=price_to)
        if price_from:
            self.queryset = self.queryset.filter(price__gte=price_from)

        return super().list(self, request, *args, **kwargs)
