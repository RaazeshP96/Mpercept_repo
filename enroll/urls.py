from django.urls import include, path
from rest_framework import routers
from . views import EnrollRetrieveUpdateDestroyView
from . import views

router = routers.DefaultRouter()
router.register(r'enroll', views.EnrollViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('<int:pk>', EnrollRetrieveUpdateDestroyView.as_view(), name='Enroll_rud'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
