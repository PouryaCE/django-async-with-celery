from celery import shared_task
from time import sleep
from task.models import UserTask
from celery.result import AsyncResult
import logging

logger = logging.getLogger(__name__)

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




@shared_task
def periodic_task_for_update_status():
    all_tasks = UserTask.objects.filter(status="PENDING")
    for task in all_tasks:
        try:
            result = AsyncResult(task.task_id)
            if result.ready():
                if result.successful():
                    task.status = 'SUCCESS'
                    task.result = result.result
                elif result.failed():
                    task.status = 'FAILURE'
                    task.result = result.traceback
                else:
                    task.status = 'STARTED'
            task.save()
        except Exception as e:
            logger.error(f"Error updating task {task.task_id}: {e}")
    logger.info("Periodic task completed")