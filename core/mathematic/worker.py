from celery import shared_task
from time import sleep


@shared_task(bind=True)
def add_numbers(self, a, b):
    sleep(10)
    return a + b



@shared_task(bind=True)
def multiple_numbers(self, a, b):
    sleep(10)
    return a * b



@shared_task(bind=True)
def divide_numbers(self, a, b):
    sleep(10)
    return a / b



@shared_task(bind=True)
def minus_numbers(self, a, b):
    sleep(10)
    return a - b