from django.core.serializers import serialize
from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics, viewsets, mixins
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from .models import Plants, Category
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .serializers import PlantsSerializer

class PlantsAPIList(generics.ListCreateAPIView):
    queryset = Plants.objects.all()
    serializer_class = PlantsSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class PlantsAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Plants.objects.all()
    serializer_class = PlantsSerializer
    permission_classes = (IsOwnerOrReadOnly, )


class PlantsAPIDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Plants.objects.all()
    serializer_class = PlantsSerializer
    permission_classes = (IsAdminOrReadOnly, )