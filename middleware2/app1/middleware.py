class FirstMiddleWare(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print('Pre-Processing-1 request')
        response = self.get_response(request)
        print('Post-Processing-1 request')
        return response


class SecondMiddleWare(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print('Pre-Processing-2 request')
        response = self.get_response(request)
        print('Post-Processing-2 request')
        return response