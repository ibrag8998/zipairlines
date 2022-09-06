from rest_framework.routers import DefaultRouter

from airplanes.views import AirplaneViewSet

router = DefaultRouter()
router.register("", AirplaneViewSet)

app_name = "airplanes"
urlpatterns = [
    *router.urls,
]
