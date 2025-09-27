import datetime
from django.http import HttpResponse

class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        now = datetime.datetime.now()
        
        response = self.get_response(request)
        user = request.user
        path = request.path
        log = f"{now} - User: {user} - Path: {path}\n"
        with open("requests.log", "a") as f:
            f.write(log)
        return response
    

class RestrictAccessByTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        now = datetime.datetime.now()
        if not (now.hour >= 18 and now.hour <= 21):
            return HttpResponse("Forbidden hours",status=403)
        response = self.get_response(request)
        return response
