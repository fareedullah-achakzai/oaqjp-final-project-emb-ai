from django.contrib import admin
from .models import Course, Lesson, Instructor, Learner, Question, Choice, Submission


class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'course', 'grade')
    inlines = [ChoiceInline]


class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'course')


admin.site.register(Course)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Submission)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Lesson, LessonAdmin)
