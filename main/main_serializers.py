# -*- coding: utf-8 -*-


from rest_framework import serializers

from main.models import Shoes

# 使用ModelSerializer来序列化model
class ShoeSerializer(serializers.ModelSerializer):
    class Meta:
        # 要序列化的模型
        model = Shoes
        # 要序列化的字段
        fields = "__all__"


