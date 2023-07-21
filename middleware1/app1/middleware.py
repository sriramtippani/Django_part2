from django.http import HttpResponse
class ErrorMessageMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_exception(self, request, exception):
        return HttpResponse('<h1>Currently we are facing a technical problems please try after some time.</h1> <h2>Raised Exception:{}</h2><h2>Exception Message:{}</h2>'.format(exception.__class__.__name__, exception))
