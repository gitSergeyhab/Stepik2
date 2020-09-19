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
