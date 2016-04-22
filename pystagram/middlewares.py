from django.http import HttpResponse



class HelloWorldError(Exception):
    pass

class SampleMiddleware(object):
    def process_request(self, request):
        request.just_say = 'Hello world'

    def process_exception(self, request, exc):
        if isinstance(exc, HelloWorldError):
            return HttpResponse('악, Hello world error...')
