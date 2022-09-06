from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from airplanes.models import Airplane


class AirplaneViewSetTest(APITestCase):
    list_url = "airplanes:airplane-list"
    detail_url = "airplanes:airplane-detail"

    def test_create_with_invalid_data(self):
        payloads = [
            {"id": 0, "passengers": 1},
            {"id": -1, "passengers": 1},
            {"id": 1, "passengers": -1},
            {"id": -2, "passengers": -2},
        ]
        for payload in payloads:
            response = self.client.post(reverse(self.list_url), data=payload)
            self.assertEqual(response.status_code, 400)

    def test_create_with_valid_data(self):
        response = self.client.post(reverse(self.list_url), data={"id": 1, "passengers": 50})
        self.assertEqual(response.status_code, 201)

        airplane = Airplane.objects.get(id=1)
        self.assertEqual(airplane.passengers, 50)

    def test_airplane_json_fields(self):
        Airplane.objects.create(id=1, passengers=111)
        response = self.client.get(reverse(self.detail_url, args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(isinstance(response.data.get("id"), int))
        self.assertTrue(isinstance(response.data.get("passengers"), int))
        self.assertTrue(isinstance(response.data.get("fuel_tank"), int))
        self.assertTrue(isinstance(response.data.get("fuel_per_minute"), float))
        self.assertTrue(isinstance(response.data.get("max_fly_minutes"), float))

    def test_correct_numbers(self):
        Airplane.objects.create(id=3, passengers=50)
        response = self.client.get(reverse(self.detail_url, args=[3]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.get("id"), 3)
        self.assertEqual(response.data.get("passengers"), 50)
        self.assertEqual(response.data.get("fuel_tank"), 600)
        self.assertEqual(response.data.get("fuel_per_minute"), 0.9788898309344879)
        self.assertEqual(response.data.get("max_fly_minutes"), 612.9392512201457)

        Airplane.objects.create(id=1, passengers=0)
        response = self.client.get(reverse(self.detail_url, args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.get("id"), 1)
        self.assertEqual(response.data.get("passengers"), 0)
        self.assertEqual(response.data.get("fuel_tank"), 200)
        self.assertEqual(response.data.get("fuel_per_minute"), 0)
        self.assertEqual(response.data.get("max_fly_minutes"), -1)

        Airplane.objects.create(id=123, passengers=4567)
        response = self.client.get(reverse(self.detail_url, args=[123]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.get("id"), 123)
        self.assertEqual(response.data.get("passengers"), 4567)
        self.assertEqual(response.data.get("fuel_tank"), 24600)
        self.assertEqual(response.data.get("fuel_per_minute"), 12.983747484297934)
        self.assertEqual(response.data.get("max_fly_minutes"), 1894.6764044626048)
