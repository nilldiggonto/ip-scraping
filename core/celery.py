from __future__ import absolute_import
from datetime import timedelta
import os
from celery import Celery
# from celery.schedules import schedule,crontab
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery("core", broker=os.environ.get('REDIS_URL', 'redis://127.0.0.1:6379/1'))

app.conf.broker_connection_retry_on_startup = True
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


app.conf.beat_schedule = {
    'add-every-5-minutes': { 
        'task': 'scrap.tasks.task_save_ip_info',
        'schedule': timedelta(days=1),
    }
}

