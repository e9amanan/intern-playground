from rest_framework import serializers
from .models import Task,Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=['id','name']


class TaskSerializer(serializers.ModelSerializer):
    category=CategorySerializer(read_only=True)

    class Meta:
        model=Task
        fields='__all__'
        read_only_fields=['created_at','updated_at','owner']



    def validate_title(self,value):
        if len(value)<3:
            raise serializers.ValidationError("Title must be at least 3 characters long.")
        return value