from django.contrib import admin
from .models import Department, Staff


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    pass


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = [
        "first_name",
        "last_name",
        "middle_name",
        "position",
        "salary",
        "age",
        "department",
    ]
    list_filter = ["age", "salary"]
    search_fields = ["first_name", "last_name", "position"]
