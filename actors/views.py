
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from actors.models import actor
from app.permisions import GlobalDefaultPermission
from actors.serializers import ActorSerializers


class ActorCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = actor.objects.all()
    serializer_class = ActorSerializers


class ActorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = actor.objects.all()
    serializer_class = ActorSerializers
