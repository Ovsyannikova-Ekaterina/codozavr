from django.contrib import admin
from .models import Course, Topic, Lesson, CourseApplication, FeedbackForm

class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'duration', 'cost', 'level']

class TopicAdmin(admin.ModelAdmin):
    list_display = ['name', 'course', 'description']

class LessonAdmin(admin.ModelAdmin):
    list_display = ['date', 'start_time', 'end_time', 'teacher', 'topic', 'application']

class CourseApplicationAdmin(admin.ModelAdmin):
    list_display = ['date', 'time', 'status', 'parent_email', 'parent_phone', 'course', 'parent']

class FeedbackFormAdmin(admin.ModelAdmin):
    list_display = ['date', 'time', 'description']

admin.site.register(Course, CourseAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(CourseApplication, CourseApplicationAdmin)
admin.site.register(FeedbackForm, FeedbackFormAdmin)
