from django.shortcuts import render
import json
from django.http import HttpResponse
# Create your views here.
def vote(request, question_id):
    resp = {'errorcode': 100, 'detail': 'Get success', 'data': r'json测试'+str(question_id)}
    return HttpResponse(json.dumps(resp,ensure_ascii=False), content_type="application/json,charset=utf-8")