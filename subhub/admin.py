from django.contrib import admin
from .models import Quiz, Question, Choice, UserQuizResponse

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1

@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'num_questions')
    inlines = [QuestionInline]

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'quiz')
    inlines = [ChoiceInline]

@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('text', 'question', 'is_correct')

@admin.register(UserQuizResponse)
class UserQuizResponseAdmin(admin.ModelAdmin):
    list_display = ('user', 'quiz', 'score', 'submitted_at')
