from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import PersonalDetails, Education, WorkExperience, Skill, Project
from .serializers import (
    PersonalDetailsSerializer, EducationSerializer, WorkExperienceSerializer,
    SkillSerializer, ProjectSerializer,
)

class PersonalDetailsListCreateAPIView(generics.ListCreateAPIView):
    queryset = PersonalDetails.objects.all()
    serializer_class = PersonalDetailsSerializer
    permission_classes = [IsAuthenticated]

class PersonalDetailsRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PersonalDetails.objects.all()
    serializer_class = PersonalDetailsSerializer
    permission_classes = [IsAuthenticated]

class EducationListCreateAPIView(generics.ListCreateAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
    permission_classes = [IsAuthenticated]

class EducationRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
    permission_classes = [IsAuthenticated]

class WorkExperienceListCreateAPIView(generics.ListCreateAPIView):
    queryset = WorkExperience.objects.all()
    serializer_class = WorkExperienceSerializer
    permission_classes = [IsAuthenticated]

class WorkExperienceRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = WorkExperience.objects.all()
    serializer_class = WorkExperienceSerializer
    permission_classes = [IsAuthenticated]

class SkillListCreateAPIView(generics.ListCreateAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [IsAuthenticated]

class SkillRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [IsAuthenticated]

class ProjectListCreateAPIView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

class ProjectRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]
