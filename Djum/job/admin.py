from django.contrib import admin

# Register your models here.
from .models import Specialties, Companies, Jobs


class JobAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category', 'company', 'salary_from', 'salary_to', 'posted']
    list_display_links = ['id', 'title']
    search_fields = ['title', 'category', 'company', ]


admin.site.register(Specialties)
admin.site.register(Companies)
admin.site.register(Jobs, JobAdmin)

# title = models.CharField(max_length=64, verbose_name="Профессия")
# category = models.CharField(max_length=32, verbose_name="Категория")
# company = models.CharField(max_length=32, verbose_name="Компания")
# salary_from = models.IntegerField(verbose_name="Зарплата от")
# salary_to = models.IntegerField(verbose_name="Зарплата до")
# posted = models.DateField(verbose_name="Дата размещения", auto_now_add=True)
# desc = models.CharField(max_length=32, verbose_name="ХЗ")
