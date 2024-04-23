from django.contrib import admin

# Register your models here.
from main_app.models import Student, Template


class StudentAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Basic Information', {'fields': ['username', 'name', 'dob', 'email_id', 'mobile_no', 'address']}),
        ('Objective in Life', {'fields': ['objective']}),
        ('Brief Overview', {'fields': ['brief_overview']}),
        ('Educational Qualification', {'fields': ['tenth_marks', 'twe_marks', 'gradu_agg']}),
        ('Extras', {'fields': ['tech_certi', 'extra_curri', 'project']})
    ]
    list_display = ['username', 'name', 'email_id', 'mobile_no']
    list_filter = ['username', 'name', 'email_id']
    search_fields = ['name', 'email_id', 'mobile_no']


admin.site.register(Student, StudentAdmin)
admin.site.register(Template)
