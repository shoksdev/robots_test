from django.db import models

from customers.models import Customer


# Добавил в модель заказа поля: модель, версия, дата создания и в каком количестве хотят заказать робота
# (для создания робота в случае его отсутсвия), а также когда был создан заказ
# (для отслеживания сколько заказов определенного робота в неделю) и сделал приятный глазу вывод
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    robot_serial = models.CharField(max_length=5, blank=False, null=False)
    robot_model = models.CharField(max_length=2, blank=False, null=False)
    robot_version = models.CharField(max_length=2, blank=False, null=False)
    robot_created = models.DateTimeField(blank=False, null=False)
    robot_quantity = models.PositiveSmallIntegerField(default=0)
    order_created = models.DateTimeField(blank=False, null=False)
