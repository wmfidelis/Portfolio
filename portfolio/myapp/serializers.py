from rest_framework import serializers
from .models import PersonalDetails, Education, WorkExperience, Skill, Project

class PersonalDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalDetails
        fields = ['id', 'full_name', 'email', 'phone_number', 'address']

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = ['id', 'institution', 'degree', 'field_of_study', 'start_date', 'end_date', 'description']

class WorkExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkExperience
        fields = ['id', 'company', 'position', 'start_date', 'end_date', 'description']

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['id', 'name', 'description']

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'start_date', 'end_date', 'url']
