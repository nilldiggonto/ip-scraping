from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from celery.result import AsyncResult

from .tasks import task_save_ip_info
# Create your views here.

def home(request):
    template_name = 'store_ip.html'
    return render(request,template_name)

class InitiateSavingIPAPIView(APIView):
    def get(self,request,*args,**kwargs):
        task_info = task_save_ip_info.delay()
        return Response({'status':'success','task_id':task_info.id})
    
class GettingTaskResult(APIView):
    def get(self,request,*args,**kwargs):
        task_id = request.GET.get('task_id')
        task_result = AsyncResult(task_id)
        if task_result.ready():
            return Response({'status':task_result.status})
        return Response({'status':'pending'})


