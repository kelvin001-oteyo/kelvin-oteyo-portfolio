from django.contrib import admin
from .models import Skill, Education, CertificationStat


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'level')


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('degree', 'institution', 'year')


@admin.register(CertificationStat)
class CertificationStatAdmin(admin.ModelAdmin):
    list_display = ('category', 'count')
