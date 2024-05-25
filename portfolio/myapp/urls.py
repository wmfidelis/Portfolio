from django.urls import path
from .views import (
    PersonalDetailsListView, PersonalDetailsCreateView, PersonalDetailsUpdateView, PersonalDetailsDeleteView,
    EducationListView, EducationCreateView, EducationUpdateView, EducationDeleteView,
    WorkExperienceListView, WorkExperienceCreateView, WorkExperienceUpdateView, WorkExperienceDeleteView,
    SkillListView, SkillCreateView, SkillUpdateView, SkillDeleteView,
    ProjectListView, ProjectCreateView, ProjectUpdateView, ProjectDeleteView,
)
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    
    path('personal-details/', PersonalDetailsListView.as_view(), name='personal_details_list'),
    path('personal-details/create/', PersonalDetailsCreateView.as_view(), name='personal_details_create'),
    path('personal-details/<int:pk>/update/', PersonalDetailsUpdateView.as_view(), name='personal_details_update'),
    path('personal-details/<int:pk>/delete/', PersonalDetailsDeleteView.as_view(), name='personal_details_delete'),

    path('education/', EducationListView.as_view(), name='education_list'),
    path('education/create/', EducationCreateView.as_view(), name='education_create'),
    path('education/<int:pk>/update/', EducationUpdateView.as_view(), name='education_update'),
    path('education/<int:pk>/delete/', EducationDeleteView.as_view(), name='education_delete'),

    path('work-experience/', WorkExperienceListView.as_view(), name='work_experience_list'),
    path('work-experience/create/', WorkExperienceCreateView.as_view(), name='work_experience_create'),
    path('work-experience/<int:pk>/update/', WorkExperienceUpdateView.as_view(), name='work_experience_update'),
    path('work-experience/<int:pk>/delete/', WorkExperienceDeleteView.as_view(), name='work_experience_delete'),

    path('skill/', SkillListView.as_view(), name='skill_list'),
    path('skill/create/', SkillCreateView.as_view(), name='skill_create'),
    path('skill/<int:pk>/update/', SkillUpdateView.as_view(), name='skill_update'),
    path('skill/<int:pk>/delete/', SkillDeleteView.as_view(), name='skill_delete'),

    path('project/', ProjectListView.as_view(), name='project_list'),
    path('project/create/', ProjectCreateView.as_view(), name='project_create'),
    path('project/<int:pk>/update/', ProjectUpdateView.as_view(), name='project_update'),
    path('project/<int:pk>/delete/', ProjectDeleteView.as_view(), name='project_delete'),
]
