from django.db.models import Count, Q
from rest_framework.generics import ListAPIView, RetrieveAPIView

from users.models import User
from users.serializers import UserSerializer


class UserListView(ListAPIView):
    queryset = User.objects.order_by('username').\
        annotate(total_ads=Count('ads', filter=Q(ads__is_published__exact=True))).\
        prefetch_related('location', 'groups', 'user_permissions').all()

    serializer_class = UserSerializer


class UserDetailView(RetrieveAPIView):
    queryset = User.objects.prefetch_related('location').all()
    serializer_class = UserSerializer
