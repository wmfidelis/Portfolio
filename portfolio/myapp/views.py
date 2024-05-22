from rest_framework import generics
from .models import PersonalDetails, Education, WorkExperience, Skill, Project
from .serializers import (
    PersonalDetailsSerializer, EducationSerializer, WorkExperienceSerializer,
    SkillSerializer, ProjectSerializer,
)

class PersonalDetailsListCreateAPIView(generics.ListCreateAPIView):
    queryset = PersonalDetails.objects.all()
    serializer_class = PersonalDetailsSerializer

class PersonalDetailsRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PersonalDetails.objects.all()
    serializer_class = PersonalDetailsSerializer

class EducationListCreateAPIView(generics.ListCreateAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer

class EducationRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer

class WorkExperienceListCreateAPIView(generics.ListCreateAPIView):
    queryset = WorkExperience.objects.all()
    serializer_class = WorkExperienceSerializer

class WorkExperienceRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = WorkExperience.objects.all()
    serializer_class = WorkExperienceSerializer

class SkillListCreateAPIView(generics.ListCreateAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

class SkillRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

class ProjectListCreateAPIView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ProjectRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
