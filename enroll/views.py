#THis is view
from django.shortcuts import render
from .models import Enroll
from rest_framework import viewsets
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from .serializers import EnrollSerializer
from django.shortcuts import render


class EnrollViewSet(viewsets.ModelViewSet):
    queryset = Enroll.objects.all()
    serializer_class = EnrollSerializer


class EnrollRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = EnrollSerializer

    def get_queryset(self):
        return Enroll.objects.all()






