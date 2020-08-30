from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Story(models.Model):
    body = RichTextUploadingField()

class Question(models.Model):
    question = models.CharField(max_length=500)
    option_1 = models.CharField(max_length=120)
    option_2 = models.CharField(max_length=50)
    option_3 = models.CharField(max_length=50)
    option_4 = models.CharField(max_length=50)

    # answer
    answer = models.CharField(max_length=50)

    def __str__(self):
        return f'Question {self.id}'

class UserAnswer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True, blank=True)
    response = models.CharField(max_length=120, null=True, blank=True)

    def __str__(self):
        return f'answer on question {self.question.id}'  

class UserQuizScore(models.Model):
    score = models.IntegerField(null=True, blank=True, default=0)
    is_attempted = models.BooleanField(default=False)
    
