import json
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.core import mail
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.utils.html import strip_tags

# Импортируем все модели и сигналы нашего проекта, а также почту, с которой будут отправляться сообщения
from R4C.settings import EMAIL_HOST_USER
from .models import Order
from customers.models import Customer
from robots.models import Robot
from robots.signals import robot_created_signal
from .signals import need_robot_signal


@method_decorator(csrf_exempt, name='dispatch')
def create_order(request):
    # Если метод запроса POST, то добавляем нового робота
    if request.method == 'POST':
        body = json.loads(request.body)  # Получаем данные из json

        # Достаём отдельные данные и записываем их в переменные
        order_customer_id = body.get('customer_id')
        order_robot_serial = body.get('robot_serial')
        order_robot_model = body.get('robot_model')
        order_robot_version = body.get('robot_version')
        order_robot_created = body.get('robot_created')
        order_robot_quantity = body.get('robot_quantity')
        json_order_created = body.get('order_created')

        # С помощью полученных выше данных находим почту покупателя, который хочет сделать заказ
        customer_email = Customer.objects.values().get(id=order_customer_id)['email']
        try:
            # Формируем словарь из полученных выше данных
            order_data = {
                "customer_id": order_customer_id,
                "robot_serial": order_robot_serial,
                "robot_model": order_robot_model,
                "robot_version": order_robot_version,
                "robot_created": order_robot_created,
                "robot_quantity": order_robot_quantity,
                "order_created": json_order_created
            }

            # Создаём Заказ
            Order.objects.create(**order_data)

            # Если робот, которого хочет купить заказчик есть в БД, оформляем заказ и вычитаем количество,
            # которое оформил Покупатель
            old_quantity = Robot.objects.get(model=order_robot_model, version=order_robot_version)
            old_quantity.quantity -= order_robot_quantity
            old_quantity.save()

            # Выводим сообщение об успешном создании заказа
            message = {
                'message': f'Вы создали заказ на приобретение робота {order_robot_model}-{order_robot_version} '
                           f'из серии: {order_robot_serial} в количестве {order_robot_quantity}!',
            }

            # Возвращаем объект класса JsonResponse со статусом 201
            return JsonResponse(message, status=201)
        except:
            # Если робота, которого хочет купить заказчик нет на складе, отправляем сигнал в приложение "robots"
            need_robot_signal.send(
                sender=create_order,
                order_customer_email=customer_email,
                order_serial=order_robot_serial,
                order_model=order_robot_model,
                order_version=order_robot_version,
                order_created=order_robot_created,
                order_quantity=order_robot_quantity
            )

            # Выводим сообщение об ошибке создания заказа, по причине отсутствия его на складе
            message = {
                'message': 'В данный момент на складе нет робота, которого вы желаете приобрести, как только он '
                           'появится мы отправим письмо на ваш адрес электронной почты.',
            }

            # Возвращаем объект класса JsonResponse со статусом 400
            return JsonResponse(message, status=400)


# Долго ломал голову как сделать так, чтобы письмо пользователю отправлялось из файла utilities.py, подобное уже
# делал на другом проекте, но, к сожалению, так и не получилось, поэтому функционал отправки письма пользователю
# на email остался в views.py
@receiver(robot_created_signal)  # Принимаем сигнал
def send_email(sender, order_customer_email, robot_model, robot_version, **kwargs):
    subject = 'Робот, которого вы заказывали теперь в наличии!'  # Тема сообщения
    context = {
        'model': robot_model,
        'version': robot_version,
    }  # Контекст сообщения, для вывода модели и версии в сообщении
    html_message = render_to_string('email/robot_in_stock_message.html', context)  # Рендерим HTML-шаблон сообщения
    plain_message = strip_tags(html_message)  # Удаляем теги из сообщения
    from_email = EMAIL_HOST_USER  # Указываем откуда отправить письмо
    to = order_customer_email  # И кому (получаем из сигнала)

    mail.send_mail(subject, plain_message, from_email, [to], html_message=html_message)  # Собираем все воедино и
    # отправляем письмо
