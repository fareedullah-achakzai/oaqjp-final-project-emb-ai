from django.contrib import admin
from .models import Question, Choice, Submission, Lesson, User, Course, Category


class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]


class LessonAdmin(admin.ModelAdmin):
    list_display = ('id',)


admin.site.register(Question, QuestionAdmin)
admin.site.register(Lesson, LessonAdmin)
