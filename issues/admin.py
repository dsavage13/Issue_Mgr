from django.contrib import admin
from .models import Issue

# Register your models here.
class IssueAdmin(admin.ModelAdmin):
    list_display = [
        "name", 
        "summary",
        "reporter", 
        "created_on"  
    ]
admin.site.register(Issue, IssueAdmin)