from django.http import JsonResponse
from django.db import connection
from django.core.exceptions import ImproperlyConfigured

def health_check(request):
    try:
        connection.ensure_connection()
        return JsonResponse({"status": "ok", "database": "connected"})
    except ImproperlyConfigured:
        return JsonResponse({"status": "error", "database": "not connected"}, status=500)
