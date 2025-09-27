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


class OffensiveLanguageMiddleware:
    def __init__(self, get_response):
        self.ips = {}
        self.get_response = get_response

    def __call__(self, request):
        x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]  # Take the first IP in the list
        else:
            ip = request.META.get("REMOTE_ADDR")
        if ip in self.ips:

            # check the number of requests
            time_of_first_request = self.ips[ip]["time_of_first_request"]
            num_of_request = self.ips[ip]["num_request"]
            now = datetime.datetime.now()
            time_diff = now - time_of_first_request 
            if time_diff.seconds < 60:
                if num_of_request >= 5:
                    return HttpResponse('Exceeded number of messages in a minute', status=403)
                else:
                    self.ips[ip]["num_request"] += 1
                    response = self.get_response(request)
                    return response
        now = datetime.datetime.now()
        self.ips[ip] = {"time_of_first_request": now, "num_request": 1 }
        response = self.get_response(request)
        return response
            

        
