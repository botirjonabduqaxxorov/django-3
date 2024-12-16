from django.contrib import admin
from .models import Course, Student, Comment

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'course', 'enrolled_at')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('course', 'student', 'created_at')
