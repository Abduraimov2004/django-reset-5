from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from olcha.models import AttributeKey, AttributeValue, ProductAttribute
from olcha.serializers import AttributeKeySerializer, AttributeValueSerializer, ProductAttributeSerializer


class AttributeKeyAPIView(APIView):
    def get(self, request, *args, **kwargs):
        attribute_keys = AttributeKey.objects.all()
        serializer = AttributeKeySerializer(attribute_keys, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = AttributeKeySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AttributeValueAPIView(APIView):
    def get(self, request, *args, **kwargs):
        attribute_values = AttributeValue.objects.all()
        serializer = AttributeValueSerializer(attribute_values, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = AttributeValueSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductAttributeAPIView(APIView):
    def get(self, request, *args, **kwargs):
        product_attributes = ProductAttribute.objects.all()
        serializer = ProductAttributeSerializer(product_attributes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = ProductAttributeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
