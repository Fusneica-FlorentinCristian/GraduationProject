from pprint import pprint

from django.db.models.fields.related import RelatedField, OneToOneField, ForeignKey
from rest_framework.views import APIView
from apps.models import UtilityType, Property
from rest_framework.response import Response
from apps.serializers.feeSerializer import UtilityTypeSerializer
from apps.serializers.propertySerializer import PropertySerializer
from itertools import chain


# Create your views here.

class BasicAPIView(APIView):
    def __init__(self, serializer, model, **kwargs):
        super().__init__(**kwargs)
        self.serializer_class = serializer
        self.model = model

    def get(self, response, detailed=False):
        detail = [self.to_dict(item, detailed) for item in self.model.objects.all()]
        return Response(detail)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    @classmethod
    def to_dict(cls, instance, depth: int):
        depth -= 1
        opts = instance._meta
        data = {}
        # pprint(opts.concrete_fields)
        # for f in chain(opts.concrete_fields, opts.private_fields):
        #     data[f.name] = f.value_from_object(instance)

        # for f in chain(opts.concrete_fields, opts.private_fields):
        for f in chain(opts.concrete_fields, opts.private_fields):
            if isinstance(f, ForeignKey):
                data[f.name] = cls.to_dict(f.related_model.objects.get(pk=f.value_from_object(instance)), depth)
            elif isinstance(f, RelatedField):
                data[f.name] = [cls.to_dict(i, depth) for i in f.value_from_object(instance)]
            elif depth <= -1 or not isinstance(f, RelatedField):
                data[f.name] = f.value_from_object(instance)
        if opts.many_to_many:
            for f in opts.many_to_many:
                if depth <= -1:
                    data[f.name] = [i.pk for i in f.value_from_object(instance)]
                else:
                    data[f.name] = [cls.to_dict(i, depth) for i in f.value_from_object(instance)]
        return data


class UtilityTypeAPIView(BasicAPIView):
    def __init__(self, serializer=UtilityTypeSerializer, model=UtilityType, **kwargs):
        super().__init__(serializer, model, **kwargs)


class PropertyAPIView(BasicAPIView):
    def __init__(self, serializer=PropertySerializer, model=Property, **kwargs):
        super().__init__(serializer, model, **kwargs)


# model_fields = [f.name for f in self.model._meta.get_fields()]
# print(model_fields)
# for item in self.model.objects.all():
#     object_dict = {}
#     for field in model_fields:
#         try:
#             info = getattr(item, field)
#             object_dict[field] = info
#             detail.append(object_dict)
#         except:
#             pass

