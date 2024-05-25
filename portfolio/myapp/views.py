from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import PersonalDetails, Education, WorkExperience, Skill, Project
from .serializers import (
    PersonalDetailsSerializer, EducationSerializer, WorkExperienceSerializer,
    SkillSerializer, ProjectSerializer,
)
from .forms import PersonalDetailsForm, EducationForm, WorkExperienceForm, SkillForm, ProjectForm


class PersonalDetailsListView(LoginRequiredMixin, ListView):
    model = PersonalDetails
    template_name = 'personal_details_list.html'
    context_object_name = 'personal_details_list'

class PersonalDetailsCreateView(LoginRequiredMixin, CreateView):
    model = PersonalDetails
    template_name = 'personal_details_form.html'
    form_class = PersonalDetailsForm
    success_url = reverse_lazy('personal_details_list')

class PersonalDetailsUpdateView(LoginRequiredMixin, UpdateView):
    model = PersonalDetails
    template_name = 'personal_details_form.html'
    form_class = PersonalDetailsForm
    success_url = reverse_lazy('personal_details_list')

class PersonalDetailsDeleteView(LoginRequiredMixin, DeleteView):
    model = PersonalDetails
    template_name = 'personal_details_confirm_delete.html'
    success_url = reverse_lazy('personal_details_list')

class EducationListView(LoginRequiredMixin, ListView):
    model = Education
    template_name = 'education_list.html'
    context_object_name = 'education_list'

class EducationCreateView(LoginRequiredMixin, CreateView):
    model = Education
    template_name = 'education_form.html'
    form_class = EducationForm
    success_url = reverse_lazy('education_list')

class EducationUpdateView(LoginRequiredMixin, UpdateView):
    model = Education
    template_name = 'education_form.html'
    form_class = EducationForm
    success_url = reverse_lazy('education_list')

class EducationDeleteView(LoginRequiredMixin, DeleteView):
    model = Education
    template_name = 'education_confirm_delete.html'
    success_url = reverse_lazy('education_list')

class WorkExperienceListView(LoginRequiredMixin, ListView):
    model = WorkExperience
    template_name = 'work_experience_list.html'
    context_object_name = 'work_experience_list'

class WorkExperienceCreateView(LoginRequiredMixin, CreateView):
    model = WorkExperience
    template_name = 'work_experience_form.html'
    form_class = WorkExperienceForm
    success_url = reverse_lazy('work_experience_list')

class WorkExperienceUpdateView(LoginRequiredMixin, UpdateView):
    model = WorkExperience
    template_name = 'work_experience_form.html'
    form_class = WorkExperienceForm
    success_url = reverse_lazy('work_experience_list')

class WorkExperienceDeleteView(LoginRequiredMixin, DeleteView):
    model = WorkExperience
    template_name = 'work_experience_confirm_delete.html'
    success_url = reverse_lazy('work_experience_list')

class SkillListView(LoginRequiredMixin, ListView):
    model = Skill
    template_name = 'skill_list.html'
    context_object_name = 'skill_list'

class SkillCreateView(LoginRequiredMixin, CreateView):
    model = Skill
    template_name = 'skill_form.html'
    form_class = SkillForm
    success_url = reverse_lazy('skill_list')

class SkillUpdateView(LoginRequiredMixin, UpdateView):
    model = Skill
    template_name = 'skill_form.html'
    form_class = SkillForm
    success_url = reverse_lazy('skill_list')

class SkillDeleteView(LoginRequiredMixin, DeleteView):
    model = Skill
    template_name = 'skill_confirm_delete.html'
    success_url = reverse_lazy('skill_list')

class ProjectListView(LoginRequiredMixin, ListView):
    model = Project
    template_name = 'project_list.html'
    context_object_name = 'project_list'

class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    template_name = 'project_form.html'
    form_class = ProjectForm
    success_url = reverse_lazy('project_list')

class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    model = Project
    template_name = 'project_form.html'
    form_class = ProjectForm
    success_url = reverse_lazy('project_list')

class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    model = Project
    template_name = 'project_confirm_delete.html'
    success_url = reverse_lazy('project_list')
