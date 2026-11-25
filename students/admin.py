from django.contrib import admin
from .models import Document, Grade, SchoolClass, Student

admin.site.site_header = "Enrollment Admin"
admin.site.site_title = "Enrollment Admin"
admin.site.index_title = "Enrollment Admin"


class GradeInline(admin.TabularInline):
    model = Grade
    extra = 1


class DocumentInline(admin.TabularInline):
    model = Document
    extra = 1


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("student_id", "last_name", "first_name", "school_class", "status", "payment")
    list_filter = ("school_class", "status", "payment")
    search_fields = ("first_name", "last_name", "student_id")
    inlines = [GradeInline, DocumentInline]


admin.site.register(SchoolClass)
