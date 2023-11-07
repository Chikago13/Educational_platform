from django.db import models

from user.models import User
from study.models import Specialization


class Teacher(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    specialization = models.ForeignKey(Specialization, on_delete=models.CASCADE)



    def __repr__(self):
        return f'{self.user}, {self.specialization}'

    def __str__(self):
        return f'{self.user} {self.specialization}'
    
    class Meta:
        verbose_name = "Учитель"
        verbose_name_plural = "Учителя"
        ordering = ["user", "specialization"]


class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    age = models.DateTimeField(verbose_name='Возраст')
    

    def __repr__(self):
        return f'{self.user}'

    def __str__(self):
        return f'{self.user}'
    
    class Meta:
        verbose_name = "Студент"
        verbose_name_plural = "Студенты"
        ordering = ["user"]


