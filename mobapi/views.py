from django.shortcuts import render


from rest_framework.views import APIView
from rest_framework.response import Response
from mobapi.serializers import MobileSerializer, MobileModelSerializer
from mobapi.models import Mobiles
# Create your views here.
class MobileView(APIView):
    def get(self, request, *args, **kwargs):
        qs = Mobiles.objects.all()
        if 'name' in request.query_params:
            qs = qs.filter(name__contains=request.query_params.get('name'))
        if 'band' in request.query_params:
            qs = qs.filter(band=request.query_params.get('band'))
        serializer = MobileSerializer(qs, many=True)
        return Response(data=serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = MobileSerializer(data=request.data)
        if serializer.is_valid():
            print(serializer.validated_data)
            Mobiles.objects.create(**serializer.validated_data)
            return Response(data='ok')
        else:
            return Response(data=serializer.errors)


class MobileDetailView(APIView):
    def get(self, request, *args, **kwargs):
        id = kwargs.get('id')
        qs = Mobiles.objects.get(id=id)
        serializer = MobileSerializer(qs)
        return Response(data=serializer.data)
    def delete(self, request, *args, **kwargs):
        id = kwargs.get('id')
        mobile = Mobiles.objects.get(id=id)
        mobile.delete()
        return Response({"msg": "deleted"})
    def put(self, request, *args, **kwargs):
        id = kwargs.get('id')
        qs = Mobiles.objects.filter(id=id)
        serializer = MobileSerializer(instance=qs, data=request.data)
        if serializer.is_valid():
            # qs.name = serializer.validated_data.get('name')
            # qs.brand = serializer.validated_data.get('brand')
            qs.update(**serializer.validated_data)
            return Response({'msg':'updated'})
        else:
            return Response(data=serializer.errors)


class MobileModelView(APIView):
    def get(self, request, *args, **kwargs):
        qs = Mobiles.objects.all()
        serializer = MobileModelSerializer(qs, many=True)
        return Response(data=serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = MobileModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)


class MobileModelDetailView(APIView):
    def get(self, request, *args, **kwargs):
        id = kwargs.get('id')
        mobile = Mobiles.objects.get(id=id)
        serializer = MobileModelSerializer(mobile)
        return Response(data=serializer.data)

    def put(self, request, *args, **kwargs):
        id = kwargs.get('id')
        mobile = Mobiles.objects.get(id=id)
        serializer = MobileModelSerializer(instance=mobile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
