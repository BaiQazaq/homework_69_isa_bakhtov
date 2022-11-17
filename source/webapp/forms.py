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


def json_articles(request, *args, **kwargs):
    if request.method == 'GET':
        return JsonResponse(serialize('json', Article.objects.all()), safe=False)
    if request.method == 'POST' and request.body:
        article = json.loads(request.body)
        try:
            article = Article.objects.create(**article)
            response = JsonResponse(article.as_dict)
            response.status_code = 201
        except Exception:
            response_data = {"detail": "Uncorrect fields"}
            response = JsonResponse(response_data)
            response.status_code = 400
        return response
    
def json_articles_delete(request, pk=None, *args, **kwargs):
    article = get_object_or_404(Article, pk=pk)
    article.delete()
    return HttpResponse(status=204)