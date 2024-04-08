from django.urls import path
from .views import home,InitiateSavingIPAPIView,GettingTaskResult

urlpatterns = [
    path('',home,name='home'),
    path('fetching/data/api/',InitiateSavingIPAPIView.as_view(),name='save_ip_info'),
    path('fetching/task/result/api/',GettingTaskResult.as_view(),name='get_task_result')
]