from django.dispatch import Signal


# Создаём сигнал, о том, что робот был создан
robot_created_signal = Signal(['order_customer_email', 'robot_model', 'robot_version'])