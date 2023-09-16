from django.db import models
from django.contrib.auth.models import User


class Review(models.Model):
    id = models.AutoField('ID Заметки', primary_key=True)
    text = models.CharField('Текст заметки',max_length=255, null = False, unique= False)
    is_done = models.BooleanField('Завершено', default= False)
    author = models.ForeignKey(User, unique=False, on_delete=models.CASCADE)

class TaskName(models.Model):
    id = models.AutoField('ID Глобальной цели', primary_key=True)
    name = models.CharField('Название глобальной цели',max_length=255, null = False, unique= False)
    author = models.ForeignKey(User, unique=False, on_delete=models.CASCADE)
    tasks_count = models.IntegerField('Количество подзадач', default = 0 )

class Inter_Task(models.Model):
    id = models.AutoField('ID цели', primary_key=True)
    task_text = models.CharField('Промежуточная цель', max_length=255, null=False, unique=False)
    is_done = models.BooleanField('Завершено', default=False)
    global_task_id =  models.ForeignKey(TaskName, unique=False, on_delete=models.CASCADE)
