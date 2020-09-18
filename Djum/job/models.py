from django.db import models


# Компании
class Companies(models.Model):
    title = models.CharField(max_length=32, verbose_name="Компания")


# Категории
class Specialties(models.Model):
    code = models.CharField(max_length=32, verbose_name="Категория")
    title = models.CharField(max_length=32, verbose_name="Категория-рус")


class Jobs(models.Model):
    title = models.CharField(max_length=64, verbose_name="Профессия")
    category = models.ForeignKey(Specialties, related_name='category', on_delete=models.CASCADE)
    company = models.ForeignKey(Companies, related_name='company', on_delete=models.CASCADE)
    salary_from = models.IntegerField(verbose_name="Зарплата от")
    salary_to = models.IntegerField(verbose_name="Зарплата до")
    posted = models.DateField(verbose_name="Дата размещения", auto_now_add=True)
    desc = models.CharField(max_length=32, verbose_name="ХЗ", blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Вакансия"
        verbose_name_plural = "Вакансии"
        ordering = ['-posted']


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

""" Категории """
specialties = [
    {"code": "frontend", "title": "Фронтенд"},
    {"code": "backend", "title": "Бэкенд"},
    {"code": "gamedev", "title": "Геймдев"},
    {"code": "devops", "title": "Девопс"},
    {"code": "design", "title": "Дизайн"},
    {"code": "products", "title": "Продукты"},
    {"code": "management", "title": "Менеджмент"},
    {"code": "testing", "title": "Тестирование"}
]

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

# for i in jobs:
#     Jobs.objects.create(title=i["title"], category=i["cat"], company=i["company"], salary_from=i["salary_from"],
#                         salary_to=i["salary_to"],  desc=i["desc"])
