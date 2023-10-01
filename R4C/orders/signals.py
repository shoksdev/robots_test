from django.dispatch import Signal


# Создаём сигнал, о том, что на складе нет робота и его нужно создать
need_robot_signal = Signal(['order_customer_email', 'order_serial', 'order_model', 'order_version', 'order_created',
                            'order_quantity'])
