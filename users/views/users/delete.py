from rest_framework.generics import DestroyAPIView

from users.models import User
from users.serializers import UserSerializer


class UserDeleteView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

