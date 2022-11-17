from django.urls import path

from webapp.views import json_echo_view, get_token, json_add, json_subtract, json_multiply, json_divide


urlpatterns = [
    path('echo/', json_echo_view, name='echo'),
    path('token/', get_token, name='token'),
    path('add/', json_add, name='json_add'),
    path('subtract/', json_subtract, name='json_subtract'),
    path('multiply/', json_multiply, name='json_multiply'),
    path('divide/', json_divide, name='json_divide')
]

