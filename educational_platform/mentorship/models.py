from datetime import date

from constant.mixin import DateTimeMixin
from django.db import models
from user.models import User


class Teacher(DateTimeMixin, models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    specialization = models.ForeignKey("study.Specialization", on_delete=models.CASCADE)

    def __repr__(self):
        return f"id-{self.id}, {self.user}, {self.specialization}"

    def __str__(self):
        return f"id-{self.id}, {self.user} {self.specialization}"

    class Meta:
        verbose_name = "Учитель"
        verbose_name_plural = "Учителя"
        ordering = ["user", "specialization", "date_created"]


class Student(DateTimeMixin, models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.FloatField(verbose_name="Рейтинг", blank=False, null=False)
    birth_year = models.DateField(verbose_name="Год рождения")

    def get_age(self):
        today = date.today()
        age = (
            today.year
            - self.birth_year.year
            - ((today.month, today.day) < (self.birth_year.month, self.birth_year.day))
        )
        return age

    def __repr__(self):
        return f"id-{self.id}, {self.user}"

    def __str__(self):
        return f"id-{self.id}, {self.user}"

    class Meta:
        verbose_name = "Студент"
        verbose_name_plural = "Студенты"
        ordering = ["user", "date_created"]


class Group(DateTimeMixin, models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    course = models.ForeignKey("study.Course", on_delete=models.CASCADE)
    students = models.ManyToManyField(Student)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __repr__(self):
        return f"{self.name}"

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "Группы"
        ordering = ["name", "date_created"]
