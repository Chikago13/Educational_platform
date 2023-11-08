from django.db import models
from datetime import date

from user.models import User
from study.models import Course, Specialization


class Teacher(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    specialization = models.ForeignKey(Specialization, on_delete=models.CASCADE)



    def __repr__(self):
        return f'id-{self.id}, {self.user}, {self.specialization}'

    def __str__(self):
        return f'id-{self.id}, {self.user} {self.specialization}'
    
    class Meta:
        verbose_name = "Учитель"
        verbose_name_plural = "Учителя"
        ordering = ["user", "specialization"]


class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.FloatField(verbose_name='Рейтинг', blank=False, null=False)
    birth_year = models.DateField(verbose_name='Год рождения')

    def get_age(self):
        today = date.today()
        age = today.year - self.birth_year.year - ((today.month, today.day) < (self.birth_year.month, self.birth_year.day))
        return age


    def __repr__(self):
        return f'id-{self.id}, {self.user}'

    def __str__(self):
        return f'id-{self.id}, {self.user}'
    
    class Meta:
        verbose_name = "Студент"
        verbose_name_plural = "Студенты"
        ordering = ["user"]


class Group(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)


    def __repr__(self):
        return f'{self.name}'

    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "Группы"
        ordering = ["name"]


