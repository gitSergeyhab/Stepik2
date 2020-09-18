from django.contrib import admin

# Register your models here.
from .models import Specialty, Company, Vacancy


class VacancyAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'specialty', 'company', 'salary_min', 'salary_max', 'published_at']
    list_display_links = ['id', 'title']
    search_fields = ['title', 'specialty', 'company', 'published_at']


class SpecialtyAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'code']
    list_display_links = ['id', 'title']
    search_fields = ['title']


class CompanyAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'location', 'employee_count']
    list_display_links = ['id', 'name']
    search_fields = ['name', 'location', 'employee_count']


admin.site.register(Specialty, SpecialtyAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Vacancy, VacancyAdmin)

# title = models.CharField(max_length=64, verbose_name="Профессия")
# category = models.CharField(max_length=32, verbose_name="Категория")
# company = models.CharField(max_length=32, verbose_name="Компания")
# salary_from = models.IntegerField(verbose_name="Зарплата от")
# salary_to = models.IntegerField(verbose_name="Зарплата до")
# posted = models.DateField(verbose_name="Дата размещения", auto_now_add=True)
# desc = models.CharField(max_length=32, verbose_name="ХЗ")
