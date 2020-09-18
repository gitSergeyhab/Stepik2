from django.db import models


# Create your models here.


# class Game(models.Model):
#     home_team = models.ForeignKey(Team, related_name='game_at_home', on_delete=models.CASCADE)
#     home_team_points = models.IntegerField()
#     rival_team = models.ForeignKey(Team, related_name='rival_game', on_delete=models.CASCADE)
#     rival_team_points = models.IntegerField()
#     date = models.DateField()
# class Author(models.Model):
#     first_name = models.CharField(max_length=30, verbose_name='имя')
#     last_name = models.CharField(max_length=30, verbose_name='фамилия')
#     birth_date = models.DateField(verbose_name='дата рождения')
#     city = models.CharField(max_length=30, verbose_name='город')

class Jobs(models.Model):
    title = models.CharField(max_length=64, verbose_name="Профессия")
    category = models.CharField(max_length=32, verbose_name="Категория")
    company = models.CharField(max_length=32, verbose_name="Компания")
    salary_from = models.IntegerField(verbose_name="Зарплата от")
    salary_to = models.IntegerField(verbose_name="Зарплата до")
    posted = models.DateField(verbose_name="Дата размещения", auto_now_add=True)
    desc = models.CharField(max_length=32, verbose_name="ХЗ")


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
