from django.db import models


# Добавил поле количества роботов на складе и сделал приятный глазу вывод
class Robot(models.Model):
    serial = models.CharField(max_length=5, blank=False, null=False)
    model = models.CharField(max_length=2, blank=False, null=False)
    version = models.CharField(max_length=2, blank=False, null=False)
    created = models.DateTimeField(blank=False, null=False)
    quantity = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return f'{self.model}-{self.version}'
