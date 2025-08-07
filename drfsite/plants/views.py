from django.core.serializers import serialize
from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Plants
from .serializers import PlantsSerializer


# class PlantsAPIView(generics.ListAPIView):
#     queryset = Plants.objects.all()
#     serializer_class = PlantsSerializer


class PlantsAPIView(APIView):
    def get(self, request):
        lst = Plants.objects.all()
        return Response({'posts': PlantsSerializer(lst, many=True).data})

    def post(self, request):
        serializer = PlantsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        post_new = Plants.objects.create(
            title=request.data['title'],
            description=request.data['description'],
            category_id=request.data['category_id']
        )

        return Response({'post': PlantsSerializer(post_new).data})


