from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
import logging
from . import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('core')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Check tasks registered
logger.debug("Tasks registered:")
for task_name in app.tasks:
    logger.debug(f" - {task_name}")