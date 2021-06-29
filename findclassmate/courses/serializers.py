from rest_framework import serializers

from .models import *

class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassModel
        fields = (
            "name",
            "title",
            "description",
            "active",
        )