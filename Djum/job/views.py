from django.shortcuts import render
from django.views import View

# Create your views here.
from django.views.generic import ListView, DetailView
from .models import Specialty, Company, Vacancy

title = 'Джуманджи'


class MainView(ListView):
    model = Specialty
    template_name = 'job/index.html'
    context_object_name = 'main_specialty'
    extra_context = {'title': title}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(MainView, self).get_context_data(**kwargs)
        context['company'] = Company.objects.all()
        return context


# – Вакансии по специализации /vacancies/cat/frontend
class ListVacSpecialties(ListView):
    template_name = 'job/vacancies.html'
    context_object_name = 'vacancies'

    # !!! =self.kwargs['slug'] - украдено из интернотов и работает, но как именно - НЕ понимаю !!!
    def get_queryset(self):
        return Vacancy.objects.filter(specialty__slug=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['flag_specialty'] = Specialty.objects.filter(slug=self.kwargs['slug'])
        return context


# – Все вакансии списком   /vacancies
class ListVacancies(ListView):
    model = Vacancy
    context_object_name = 'vacancies'
    template_name = 'job/vacancies.html'


# # – Карточка компании  /companies/345
# class CardCompany(DetailView):
#     model = Company
#     context_object_name = 'company'
#     template_name = 'job/company.html'


# – Одна вакансия /vacancies/22
class OneVacancy(DetailView):
    pass


# – Карточка компании  /companies/345
class CardCompany(ListView):
    template_name = 'job/vacancies.html'
    context_object_name = 'vacancies'

    def get_queryset(self):
        return Vacancy.objects.filter(company__pk=self.kwargs['pk'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['flag_company'] = Company.objects.filter(pk=self.kwargs['pk'])
        return context
