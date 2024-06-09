from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from reviews.models import Review
from app.permisions import GlobalDefaultPermission
from reviews.serializers import ReviewSerializers


class ReviewCreatListview(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Review.objects.all()
    serializer_class = ReviewSerializers


class ReviewRetriveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Review.objects.all()
    serializer_class = ReviewSerializers
