from django.shortcuts import render
from django.views import View

# Create your views here.
from django.views.generic import ListView, DetailView
from .models import Specialty, Company, Vacancy


class MainView(ListView):
    model = Specialty
    template_name = 'job/index.html'


# – Все вакансии списком   /vacancies
class ListVacancy(ListView):
    pass


# – Вакансии по специализации /vacancies/cat/frontend
class ListVacancySpec(ListView):
    pass


# – Карточка компании  /companies/345
class CardComp(DetailView):
    pass


# – Одна вакансия /vacancies/22
class Vacancy(DetailView):
    pass
