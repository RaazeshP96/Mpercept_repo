from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Enroll


class EnrollSerializer(serializers.ModelSerializer):
    email = serializers.CharField(
        max_length=100,
        validators=[UniqueValidator(queryset=Enroll.objects.all(), message="This email already exists")]
    )

    class Meta:
        model = Enroll
        fields = '__all__'


