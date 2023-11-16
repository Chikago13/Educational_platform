from constant.mixin import DateTimeMixin
from django.db import models
from mentorship.models import Teacher
from study.models import Topic


class Test(DateTimeMixin, models.Model):
    name = models.CharField(max_length=200, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    is_open = models.BooleanField(default=False)
    create_by = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    topic = models.OneToOneField(Topic, on_delete=models.CASCADE)
    time_limit = models.PositiveSmallIntegerField(
        verbose_name="Ограничение времени для теста"
    )

    def __repr__(self):
        return f"id-{self.pk}, {self.name}, {self.description}"

    def __str__(self):
        return f"id-{self.pk}, {self.name}, {self.description}"

    class Meta:
        verbose_name = "Тест"
        verbose_name_plural = "Тесты"
        ordering = ["name", "description", "date_created"]


class Question(DateTimeMixin, models.Model):
    text = models.TextField(verbose_name="Описание")
    test = models.ForeignKey(Test, on_delete=models.CASCADE)

    def __repr__(self):
        return f"id-{self.pk}, {self.text}"

    def __str__(self):
        return f"id-{self.pk}, {self.text}"

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"
        ordering = ["text", "date_created"]


class Answer(DateTimeMixin, models.Model):
    text = models.TextField(verbose_name="Описание")
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    is_correct = models.BooleanField(default=False)

    def __repr__(self):
        return f"id-{self.pk}, {self.text}"

    def __str__(self):
        return f"id-{self.pk}, {self.text}"

    class Meta:
        verbose_name = "Ответ"
        verbose_name_plural = "Ответы"
        ordering = ["text", "date_created"]
