import math

from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from airplanes.models import Airplane


class AirplaneSerializer(ModelSerializer):
    fuel_tank = SerializerMethodField()
    fuel_per_minute = SerializerMethodField()
    max_fly_minutes = SerializerMethodField()

    class Meta:
        model = Airplane
        fields = ["id", "passengers", "fuel_tank", "fuel_per_minute", "max_fly_minutes"]
        extra_kwargs = {
            "id": {"min_value": 1},
            "passengers": {"min_value": 0},
        }

    def get_fuel_tank(self, airplane: Airplane) -> int:
        return airplane.id * 200

    def get_fuel_per_minute(self, airplane: Airplane) -> float:
        # logarithm base is not mentioned, so I used default: e.
        return math.log(airplane.id) * 0.8 + airplane.passengers * 0.002

    def get_max_fly_minutes(self, airplane: Airplane) -> float:
        try:
            return self.get_fuel_tank(airplane) / self.get_fuel_per_minute(airplane)
        except ZeroDivisionError:
            return -1
