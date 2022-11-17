import json
from django.http import HttpResponse, HttpResponseNotAllowed, JsonResponse
from datetime import datetime
from django.views.decorators.csrf import ensure_csrf_cookie
from django.core.serializers import serialize
from django.shortcuts import get_object_or_404


def json_echo_view(request, *args, **kwargs):
    answer = {
        'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'method': request.method
    }
    
    if request.body:
        answer['answer'] = json.loads(request.body)
    return JsonResponse(answer)

@ensure_csrf_cookie
def get_token(request, *rgs, **kwargs):
    if request.method == 'GET':
        return HttpResponse()
    return HttpResponseNotAllowed(f'Only GET request are allowed {request.method}')


def json_add(request, *args, **kwargs):
    if request.method == 'POST' and request.body :
        answer = {}
        nums = json.loads(request.body)
        try:
            answer['answer'] =  (nums['A']+(nums['B']))
            response = JsonResponse(answer)
        except TypeError:
            answer['error'] = "Both values must be number" 
            response = JsonResponse(answer)
            response.status_code = 400
        except ValueError:
            answer['error'] = "Strings cannot be used for mathematical operations" 
            response = JsonResponse(answer)
            response.status_code = 400
        except Exception:
            answer['error'] = "What else is this?" 
            response = JsonResponse(answer)
            response.status_code = 400
        return response
    
def json_subtract(request, *args, **kwargs):
    if request.method == 'POST' and request.body :
        answer = {}
        nums = json.loads(request.body)
        try:
            answer['answer'] =  (nums['A']-(nums['B']))
            response = JsonResponse(answer)
        except TypeError:
            answer['error'] = "Both values must be number" 
            response = JsonResponse(answer)
            response.status_code = 400
        except ValueError:
            answer['error'] = "Strings cannot be used for mathematical operations" 
            response = JsonResponse(answer)
            response.status_code = 400
        except Exception:
            answer['error'] = "What else is this?" 
            response = JsonResponse(answer)
            response.status_code = 400
        return response
    
def json_multiply(request, *args, **kwargs):
    if request.method == 'POST' and request.body :
        answer = {}
        nums = json.loads(request.body)
        try:
            answer['answer'] =  (nums['A']*(nums['B']))
            response = JsonResponse(answer)
        except TypeError:
            answer['error'] = "Both values must be number" 
            response = JsonResponse(answer)
            response.status_code = 400
        except ValueError:
            answer['error'] = "Strings cannot be used for mathematical operations" 
            response = JsonResponse(answer)
            response.status_code = 400
        except Exception:
            answer['error'] = "What else is this?" 
            response = JsonResponse(answer)
            response.status_code = 400
        return response
    
def json_divide(request, *args, **kwargs):
    if request.method == 'POST' and request.body :
        answer = {}
        nums = json.loads(request.body)
        try:
            answer['answer'] =  (nums['A']/(nums['B']))
            response = JsonResponse(answer)
        except TypeError:
            answer['error'] = "Both values must be number" 
            response = JsonResponse(answer)
            response.status_code = 400
        except ValueError:
            answer['error'] = "Strings cannot be used for mathematical operations" 
            response = JsonResponse(answer)
            response.status_code = 400
        except ZeroDivisionError:
            answer['error'] = "Division by zero!" 
            response = JsonResponse(answer)
            response.status_code = 400
        except Exception:
            answer['error'] = "What else is this?" 
            response = JsonResponse(answer)
            response.status_code = 400
        return response
