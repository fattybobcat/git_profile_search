from django.shortcuts import render

from .utils import api_pull_request_user

token = "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"
username = "fattybobcat"


def index(request):
    context = {}
    return render(request, 'index.html', context)


def search(request):
    context = {}
    if 'q' in request.GET:
        request_params = request.GET["q"].split("?")
        user_name = request.GET["q"].split("?")[0]
        params_page = ""
        if len(request_params) > 1:
            params_page = request.GET["q"].split("?")[1]
        if user_name != '':
            message = "You searched for: %r" % request.GET["q"]
            total_count, data, page = api_pull_request_user(request,
                                                            user_name,
                                                            params_page)
            context["user_name"] = user_name
            context["message"] = message
            context["total_count"] = total_count
            context["projects"] = data
            context["page"] = page
            return render(request, 'searchForm.html', context)
        message = 'You submitted an empty form.'
    else:
        message = 'You submitted an empty form.'
    context["message"] = message
    return render(request, 'index.html', context)
