from django.db import models

# Create your models here.

class myModel(models.Model):
    question_text = models.CharField(max_length=200)
