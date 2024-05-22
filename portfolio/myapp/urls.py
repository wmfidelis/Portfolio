from django.urls import path
from .views import (
    PersonalDetailsListCreateAPIView, PersonalDetailsRetrieveUpdateDestroyAPIView,
    EducationListCreateAPIView, EducationRetrieveUpdateDestroyAPIView,
    WorkExperienceListCreateAPIView, WorkExperienceRetrieveUpdateDestroyAPIView,
    SkillListCreateAPIView, SkillRetrieveUpdateDestroyAPIView,
    ProjectListCreateAPIView, ProjectRetrieveUpdateDestroyAPIView,
)

urlpatterns = [
    path('personal-details/', PersonalDetailsListCreateAPIView.as_view(), name='personal-details-list-create'),
    path('personal-details/<int:pk>/', PersonalDetailsRetrieveUpdateDestroyAPIView.as_view(), name='personal-details-detail'),

    path('education/', EducationListCreateAPIView.as_view(), name='education-list-create'),
    path('education/<int:pk>/', EducationRetrieveUpdateDestroyAPIView.as_view(), name='education-detail'),

    path('work-experience/', WorkExperienceListCreateAPIView.as_view(), name='work-experience-list-create'),
    path('work-experience/<int:pk>/', WorkExperienceRetrieveUpdateDestroyAPIView.as_view(), name='work-experience-detail'),

    path('skill/', SkillListCreateAPIView.as_view(), name='skill-list-create'),
    path('skill/<int:pk>/', SkillRetrieveUpdateDestroyAPIView.as_view(), name='skill-detail'),

    path('project/', ProjectListCreateAPIView.as_view(), name='project-list-create'),
    path('project/<int:pk>/', ProjectRetrieveUpdateDestroyAPIView.as_view(), name='project-detail'),
]
