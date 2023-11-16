from ckeditor.fields import RichTextField
from constant.mixin import DateTimeMixin
from django.db import models
from mentorship.models import Teacher


class Specialization(DateTimeMixin, models.Model):
    name = models.CharField(max_length=150, verbose_name="Название")

    def __repr__(self):
        return f"id-{self.pk}, {self.name}"

    def __str__(self):
        return f"id-{self.pk}, {self.name}"

    class Meta:
        verbose_name = "Специализация"
        verbose_name_plural = "Специализации"
        ordering = ["name", "date_created"]


class Course(DateTimeMixin, models.Model):
    name = models.CharField(max_length=150, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    specialization = models.ManyToManyField(Specialization)

    def __repr__(self):
        return f"id-{self.pk}, {self.name}, {self.description}"

    def __str__(self):
        return f"id-{self.pk}, {self.name}, {self.description}"

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"
        ordering = ["name", "description", "date_created"]


class Article(DateTimeMixin, models.Model):
    title = models.CharField(max_length=150, verbose_name="Название")
    content = RichTextField(verbose_name="Контент")
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __repr__(self):
        return f"id-{self.pk}, {self.title}, {self.content}"

    def __str__(self):
        return f"id-{self.pk}, {self.title}, {self.content}"

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
        ordering = ["title", "content", "date_created"]


class Image(DateTimeMixin, models.Model):
    # Добавляем поле для изображения
    image = models.ImageField(upload_to="images/")

    def __repr__(self):
        return f"id-{self.pk}, {self.image}"

    def __str__(self):
        return f"id-{self.pk}, {self.image}"

    class Meta:
        verbose_name = "Изоброжение"
        verbose_name_plural = "Изоброжения"
        ordering = ["image", "date_created"]


class Topic(DateTimeMixin, models.Model):
    name = models.CharField(max_length=200, verbose_name="Название")
    content = models.TextField(verbose_name="Контент")
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    images = models.ManyToManyField(Image, related_name="topics")

    def __repr__(self):
        return f"id-{self.pk}, {self.name}, {self.content}"

    def __str__(self):
        return f"id-{self.pk}, {self.name}, {self.content}"

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
        ordering = ["name", "content", "date_created"]
