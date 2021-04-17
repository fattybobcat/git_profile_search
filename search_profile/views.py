from django.shortcuts import render
import requests
from .utils import api_pull_request_user, api_project_info, sort_data_by_params
import json
from github import Github

token = "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"
username = "fattybobcat"

def index(request):
    context = {}
    return render(request, 'index.html', context)

def search(request):
    context = {}
    #print("request", request.GET['q'])
    #print("request.method", request.method )
    if 'q' in request.GET:
        user_name = request.GET["q"]
        print("user_name", user_name)
        print(type(user_name))
        if user_name != '':
            message = "You searched for: %r" % request.GET["q"]
            total_count, data = api_pull_request_user(user_name)
            context["user_name"] = user_name
            context["message"] = message
            context["total_count"] =total_count
            context["projects"] = data
            return render(request, 'searchForm.html', context)
        message = 'You submitted an empty form.'
    else:
        message = 'You submitted an empty form.'
    context["message"] = message
    return render(request, 'index.html', context)