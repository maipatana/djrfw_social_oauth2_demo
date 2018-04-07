from django.contrib.auth.models import User
from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from .models import UserProfile
from .serializers import UserSerializer, UserProfileSerializer
from .permissions import IsOwnerOrReadOnly, IsProfileOwnerOrReadOnly, IsOwner
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    lookup_field = 'username'


class CurrentUserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that return the current user.
    """
    permission_classes = (IsOwner, IsAuthenticated)
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = UserProfile.objects.all()
        return queryset

    def get_object(self):
        return self.request.user

    def list(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)