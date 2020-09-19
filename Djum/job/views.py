from django.shortcuts import render
from django.views import View

# Create your views here.
from django.views.generic import ListView, DetailView
from .models import Specialty, Company, Vacancy

title = 'Джуманджи'


class MainView(ListView):
    model = Specialty
    template_name = 'job/index.html'
    context_object_name = 'main_specy'
    extra_context = {'title': title}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(MainView, self).get_context_data(**kwargs)
        context['company'] = Company.objects.all()
        return context


# – Все вакансии списком   /vacancies
class ListVacancies(ListView):
    model = Vacancy
    context_object_name = 'list_vacancies'
    template_name = 'job/vacancies.html'


# – Вакансии по специализации /vacancies/cat/frontend
class ListVacancySpec(ListView):
    pass


# – Карточка компании  /companies/345
class CardComp(DetailView):
    pass


# – Одна вакансия /vacancies/22
class Vacancy(DetailView):
    pass
