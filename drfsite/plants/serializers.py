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


class PlantsSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    description = serializers.CharField()
    time_create = serializers.DateTimeField(read_only=True)
    time_update= serializers.DateTimeField(read_only=True)
    is_published = serializers.BooleanField(default=True)
    category_id = serializers.IntegerField()

    def create(self, validated_data):
        return Plants.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.description = validated_data.get("description", instance.description)
        instance.time_update = validated_data.get("time_update", instance.time_update)
        instance.is_published = validated_data.get("is_published", instance.is_published)
        instance.category_id = validated_data.get("category_id", instance.category_id)
        instance.save()
        return instance

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