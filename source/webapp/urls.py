from django.urls import path

from webapp.views import json_echo_view, get_token, json_add, json_substract, json_multiply, json_divide, index


urlpatterns = [
    path('echo/', json_echo_view, name='echo'),
    path('token/', get_token, name='token'),
    path('add/', json_add, name='json_add'),
    path('substract/', json_substract, name='json_substract'),
    path('multiply/', json_multiply, name='json_multiply'),
    path('divide/', json_divide, name='json_divide'),
    path('', index, name='index')
]

