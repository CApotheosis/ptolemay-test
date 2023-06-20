from rest_framework import serializers
from .models import Department, Staff


class DepartmentSerializer(serializers.Serializer):
    name = serializers.CharField()
    staff_count = serializers.IntegerField()
    total_salary = serializers.IntegerField()


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = "__all__"
