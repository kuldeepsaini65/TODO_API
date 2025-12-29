from django.conf import settings
from django.http import JsonResponse

class APIKeyAuthMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        print("PATH:", request.path)
        if not request.path.startswith("/api/"):
            return self.get_response(request)

        api_key = request.headers.get('X-API-KEY')

        if not api_key:
            return JsonResponse(
                {'status': 'error', 'message': 'API key is missing mere bhai'},
                status=401
            )

        if api_key not in settings.API_KEYS:
            return JsonResponse(
                {'status': 'error', 'message': 'Oops!! Invalid API key, Apko Galat API Key di gyi hai..'},
                status=401
            )

        request.api_key = api_key
        return self.get_response(request)
