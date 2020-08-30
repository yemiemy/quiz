from django.contrib import admin
from .models import Question, UserQuizScore, UserAnswer, Story
# Register your models here.
admin.site.register(Story)
admin.site.register(Question)
admin.site.register(UserQuizScore)
admin.site.register(UserAnswer)