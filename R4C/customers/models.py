from django.db import models


# Почти ничего не изменяем в модели Покупателя, только добавляем приятный глазу вывод
class Customer(models.Model):
    email = models.CharField(max_length=255, blank=False, null=False)

    def __str__(self):
        return self.email
