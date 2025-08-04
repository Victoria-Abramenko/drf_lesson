from django.shortcuts import render
from rest_framework import generics

from .models import Plants
from .serializers import PlantsSerializer


class PlantsAPIView(generics.ListAPIView):
    queryset = Plants.objects.all()
    serializer_class = PlantsSerializer


