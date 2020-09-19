from django.db import models
from random import choice, shuffle


class Company(models.Model):
    name = models.CharField(max_length=32, verbose_name="Компания")
    location = models.CharField(max_length=32, verbose_name="Город", blank=True)
    logo = models.ImageField(verbose_name="Логотип", upload_to="logs/%Y/%m/%d/", blank=True)
    description = models.TextField(verbose_name="Информация о компании", blank=True)
    employee_count = models.IntegerField(verbose_name="Количество сотрудников", null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Компания"
        verbose_name_plural = "Компании"


class Specialty(models.Model):
    code = models.CharField(max_length=32, verbose_name="Код")
    title = models.CharField(max_length=32, verbose_name="Специализация")
    picture = models.ImageField(verbose_name="Картинка", upload_to="pics/%Y/%m/%d/", blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Специализация"
        verbose_name_plural = "Специализации"


class Vacancy(models.Model):
    title = models.CharField(max_length=64, verbose_name="Профессия")
    specialty = models.ForeignKey(Specialty, related_name="vacancies", on_delete=models.CASCADE)
    company = models.ForeignKey(Company, related_name="vacancies", on_delete=models.CASCADE)
    skills = models.TextField(verbose_name="Навыки")
    description = models.TextField(verbose_name="Описание", blank=True)
    salary_min = models.IntegerField(verbose_name="Зарплата от")
    salary_max = models.IntegerField(verbose_name="Зарплата до")
    published_at = models.DateField(verbose_name="Опубликовано", auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Вакансия"
        verbose_name_plural = "Вакансии"
        ordering = ['-published_at']


""" Компании """
companies = [
    {"title": "workiro"},
    {"title": "rebelrage"},
    {"title": "staffingsmarter"},
    {"title": "evilthreat h"},
    {"title": "hirey "},
    {"title": "swiftattack"},
    {"title": "troller"},
    {"title": "primalassault"}
]

cities = ['Пермь', 'Санкт-Петербург', 'Екатеринбург', 'Нижний Новгород',
          'Новосибирск', 'Красноярск', 'Казань', 'Москва']

# уже выполнено - раскомментировать при создании базы данных  и импорт рандом!
# for com in companies:
#     Company.objects.create(name=com['title'], location=choice(cities), employee_count=choice(list(range(1,500))))


""" Категории """
specialties = [
    {"code": "frontend", "title": "Фронтенд"},
    {"code": "backend", "title": "Бэкенд"},
    {"code": "gamedev", "title": "Геймдев"},
    {"code": "devops", "title": "Девопс"},
    {"code": "design", "title": "Дизайн"},
    {"code": "products", "title": "Продукты"},
    {"code": "management", "title": "Менеджмент"},
    {"code": "testing", "title": "Тестирование"},
]

# уже выполнено  - раскомментировать при создании базы данных
# for sp in specialties:
#     Specialty.objects.create(code=sp['code'], title=sp['title'])


jobs = [
    {"title": "Разработчик на Python", "cat": "backend", "company": "staffingsmarter", "salary_from": "100000",
     "salary_to": "150000", "posted": "2020-03-11", "desc": "Потом добавим"},
    {"title": "Разработчик в проект на Django", "cat": "backend", "company": "swiftattack", "salary_from": "80000",
     "salary_to": "90000", "posted": "2020-03-11", "desc": "Потом добавим"},
    {"title": "Разработчик на Swift в аутсорс компанию", "cat": "backend", "company": "swiftattack",
     "salary_from": "120000", "salary_to": "150000", "posted": "2020-03-11", "desc": "Потом добавим"},
    {"title": "Мидл программист на Python", "cat": "backend", "company": "workiro", "salary_from": "80000",
     "salary_to": "90000", "posted": "2020-03-11", "desc": "Потом добавим"},
    {"title": "Питонист в стартап", "cat": "backend", "company": "primalassault", "salary_from": "120000",
     "salary_to": "150000", "posted": "2020-03-11", "desc": "Потом добавим"}
]

skillist = ['Python', 'Django', 'Flask', 'PHP', 'JS', 'Node', 'Vue', 'React', 'Git', 'SQL', 'CSS', 'HTML',
            'Ruby', 'Rails', 'Laravel', 'Spring', 'Angular', 'Ember', 'правапессанее', 'и чтоб человек хороший']


def skill_maker(x):
    shuffle(skillist)
    xx = list(range(x - 1, x + 1))
    return ' • '.join(skillist[:choice(xx)])

# уже выполнено - раскомментировать при создании базы данных  и импорт рандом!
# for j in jobs:
#     Vacancy.objects.create(title=j['title'],
#                            specialty=Specialty.objects.filter(code=j['cat'])[0],
#                            company=Company.objects.filter(name=j['company'])[0],
#                            skills=skill_maker(4), description=j['desc'],
#                            salary_min=j['salary_from'], salary_max=j['salary_to'])
#
