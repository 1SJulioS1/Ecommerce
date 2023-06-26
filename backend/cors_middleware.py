from django.middleware import csrf

def my_custom_middleware(get_response):
    def middleware(request):
        response = get_response(request)
        response['Access-Control-Allow-Origin'] = 'http://localhost:3000'
        response['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE'
        response['Access-Control-Allow-Headers'] = 'Content-Type'
        return response
    return middleware
