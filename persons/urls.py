from django.urls import path, include
from persons import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'persons', views.PersonViewSet)

urlpatterns = [
    path('', include(router.urls))
]