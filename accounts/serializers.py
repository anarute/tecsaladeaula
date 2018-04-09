from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import City, Occupation, Discipline, EducationDegree


class TimtecUserSerializer(serializers.ModelSerializer):
    name = serializers.Field(source='get_full_name')
    picture = serializers.Field(source='get_picture_url')

    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'name', 'first_name', 'last_name', 'biography', 'picture',)


class TimtecUserAdminSerializer(TimtecUserSerializer):

    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'name', 'email', 'is_active', 'is_superuser', 'first_name', 'last_name',)

class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City

class OccupationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Occupation

class DisciplineSerializer(serializers.ModelSerializer):

    class Meta:
        model = Discipline

class EducationDegreeSerializer(serializers.ModelSerializer):

    class Meta:
        model = EducationDegree

class TimtecProfileSerializer(serializers.ModelSerializer):
    city = CitySerializer(required=False)
    occupations = OccupationSerializer(many=True, required=False)
    disciplines = DisciplineSerializer(many=True, required=False)
    education_degrees = EducationDegreeSerializer(required=False, many=True)

    class Meta:
        model = get_user_model()
        fields = ('city', 'occupations', 'disciplines', 'education_degrees')