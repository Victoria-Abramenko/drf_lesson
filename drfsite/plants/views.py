from django.core.serializers import serialize
from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics, viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from .models import Plants, Category
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .serializers import PlantsSerializer


class PlantsAPIListPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 10


class PlantsAPIList(generics.ListCreateAPIView):
    queryset = Plants.objects.all()
    serializer_class = PlantsSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    pagination_class = PlantsAPIListPagination


class PlantsAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Plants.objects.all()
    serializer_class = PlantsSerializer
    permission_classes = (IsAuthenticated, )
    # authentication_classes = (TokenAuthentication, )



class PlantsAPIDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Plants.objects.all()
    serializer_class = PlantsSerializer
    permission_classes = (IsAdminOrReadOnly, )