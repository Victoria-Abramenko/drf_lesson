from django.core.serializers import serialize
from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics, viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from .models import Plants, Category
from .serializers import PlantsSerializer


class PlantsViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    # queryset = Plants.objects.all()
    serializer_class = PlantsSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')

        if not pk:
            return Plants.objects.all()[:3]

        return Plants.objects.filter(pk=pk)

    @action(methods=['get'], detail=True)
    def get_category(self, request, pk=None):
        categories = Category.objects.get(pk=pk)
        return Response({'categories': categories.category_name})


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





