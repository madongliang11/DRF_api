import re

from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from main.main_serializers import ShoeSerializer
from main.models import Shoes


@api_view(['GET'])
def get_user_shoes(request):
    """
      列出用户所有鞋子。
      get请求参数: user_id :: 用户id
    """
    user_id = request.GET.get("user_id","")
    # 校验参数...
    if user_id.isdigit():
        user_id  = int(user_id)
        shoes = Shoes.objects.filter(is_delete=False,user_id=user_id)
        serializer = ShoeSerializer(shoes, many=True)
        return Response(serializer.data)
    return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def update_user_shoes(request):
    """
      上传数据
      post参数:
    """
    serializer = ShoeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_404_NOT_FOUND)