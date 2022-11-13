from django.contrib import admin
from .models import Job,Applicant,Contact 

class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'company_name')
    list_filter = ("category","company_name",)

class ApplicantAdmin(admin.ModelAdmin):
    list_display = ('user', 'job')
    list_filter = ("job","user",)


admin.site.register(Job,JobAdmin)
admin.site.register(Contact)
admin.site.register(Applicant,ApplicantAdmin)

# Register your models here.
