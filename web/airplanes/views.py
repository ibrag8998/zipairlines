from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from airplanes.models import Airplane
from airplanes.serializers import AirplaneSerializer


class AirplaneViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    GenericViewSet
):
    queryset = Airplane.objects.all()
    serializer_class = AirplaneSerializer
