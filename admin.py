from django.contrib import admin
from . import models

class DepartmentAdmin(admin.ModelAdmin):
    #list_editable = ()
    list_per_page = 5
    list_max_show_all = 5
    list_display=('department_name',)
admin.site.register(models.Department,DepartmentAdmin)


class ProgramsAdmin(admin.ModelAdmin):
      #list_editable = ()
    list_per_page = 5
    list_max_show_all = 5
    list_display=('program_name','program_duration','date_registered','department',)
admin.site.register(models.Programs,ProgramsAdmin)


class CourseAdmin(admin.ModelAdmin):
    list_editable = ('program',)
    list_per_page = 5
    list_max_show_all = 5
    list_display=('course_name','program',)
admin.site.register(models.Course,CourseAdmin)


class AnnouncementsAdmin(admin.ModelAdmin):
    list_editable = ('file','title',)
    list_per_page = 8
    list_max_show_all = 8
    list_display=('heading','title','date_registered','file',)
admin.site.register(models.Announcements,AnnouncementsAdmin)


class HerroesAdmin(admin.ModelAdmin):
    list_per_page = 8
    list_max_show_all = 8
    list_display=('Student_name','heading','title','image_tag','date_registered','program',)
admin.site.register(models.Herroes,HerroesAdmin)


class studentAdmin(admin.ModelAdmin):
    list_editable = ('program',)
    list_per_page = 8
    list_max_show_all = 8
    list_display=('Student_name','regno','image_tag','date_registered','program',)
admin.site.register(models.student,studentAdmin)
class applicationAdmin(admin.ModelAdmin):
   
    list_per_page = 8
    list_max_show_all = 8
    list_display=('Student_name','gender','Course','faculty','department','academic_year','project_title','date_registered','research_document','image','status',)
admin.site.register(models.application,applicationAdmin)

 
 