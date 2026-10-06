from django.contrib import admin
from .models import Education, Experience, Project, Skill


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'level', 'order')
    list_editable = ('level', 'order')
    list_filter = ('category',)


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'start_date', 'end_date', 'order')
    list_editable = ('order',)


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('degree', 'institution', 'year_end', 'order')
    list_editable = ('order',)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'is_featured', 'order')
    list_editable = ('is_featured', 'order')
    prepopulated_fields = {'slug': ('title',)}
