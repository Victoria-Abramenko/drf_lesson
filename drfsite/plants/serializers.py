import io
from email.policy import default

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from .models import Plants


# class PlantsModel:
#     def __init__(self, title, description):
#         self.title = title
#         self.description = description


class PlantsSerializer(serializers.ModelSerializer):
   class Meta:
       model = Plants
       fields = "__all__"
       # fields = ("title", "description", "category")

    # def delete(self, request, *args, **kwargs):
    #     pk = kwargs.get("pk", None)
    #     if not pk:
    #         return Response({"error": "Удаление не может быть выполнено"})
    #
    #     return Response({"post": "delete post " + str(pk)})




# def encode():
#     model = PlantsModel('Echeveria Laui', 'description of succulent')
#     model_sr = PlantsSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep='/n')
#     json = JSONRenderer().render(model_sr.data)
#     print(json)
#
# def encode():
#     stream = io.BytesIO(b'{"title":"Echeveria Laui","description":"description of succulent"}')
#     data = JSONParser().parse(stream)
#     serializer = PlantsSerializer(data=data)
#     print(serializer.validated_data)