from django.shortcuts import render
import requests
import json
from github import Github
def sort_data_by_parans(data):
    
# Create your views here.
def api_s(request, user):
    # addr = 'https://api.github.com/users/' + user
    # r = requests.get(addr)
    t = user
    addr_request = "https://api.github.com/search/issues?q=author%3A{}+type%3Apr+is%3Amerged".format(t)
    data = requests.get(addr_request).json()
    c = ""
    print("data", data)
    #issue = Github.search_issues('', state='open', author='fattybobcat', type='pr')
    print(data)
    return data


def index(request):
    context = {}
    return render(request, 'index.html', context)


def search(request):
    context = {}
    print("request", request.GET['q'])
    print("request.method", request.method )
    if 'q' in request.GET:
        message = "You searched for: %r" % request.GET["q"]
        user_name = request.GET["q"]
        data = api_s(request, user_name)
        context["user_name"] = user_name
        context["message"] = message
        #print("data", data.GET["q"])
        context["total_count"] = data["total_count"]

    else:
        message = 'You submitted an empty form.'
    context["message"] = message
    return render(request, 'index.html', context)