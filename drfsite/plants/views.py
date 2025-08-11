from django.core.serializers import serialize
from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Plants
from .serializers import PlantsSerializer


class PlantsViewSet(viewsets.ModelViewSet):
    queryset = Plants.objects.all()
    serializer_class = PlantsSerializer


# class PlantsAPIView(generics.ListAPIView):
#     queryset = Plants.objects.all()
#     serializer_class = PlantsSerializer

# class PlantsApiList(generics.ListCreateAPIView):
#     queryset = Plants.objects.all()
#     serializer_class = PlantsSerializer
#
#
# class PlantsApiUpdate(generics.UpdateAPIView):
#     queryset = Plants.objects.all()
#     serializer_class = PlantsSerializer
#
#
# class PlantsApiDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Plants.objects.all()
#     serializer_class = PlantsSerializer





