import time
from celery import shared_task
from .utils import save_ip_info

@shared_task
def task_save_ip_info():
    res = save_ip_info()
    return res
