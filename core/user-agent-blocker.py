from django.http import HttpResponse
import re

class ChromeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user_agent = request.META.get('HTTP_USER_AGENT', '')
        if 'chrome' in user_agent.lower():
            return HttpResponse(status=499)

        return self.get_response(request)