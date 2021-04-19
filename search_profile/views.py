from django.shortcuts import render

from .utils import api_pull_request_user, api_search_user


def index(request):
    context = {}
    return render(request, "index.html", context)


def search(request):
    context = {}
    if 'q' in request.GET:
        request_params = request.GET["q"].split("?")
        user_name = request.GET["q"].split("?")[0]
        params_page = ""
        if len(request_params) > 1:
            params_page = request.GET["q"].split("?")[1]
        if user_name != "":
            if api_search_user(user_name) == 200:
                message = "You searched for: %r" % request.GET["q"]
                total_count, data, page = api_pull_request_user(user_name,
                                                                params_page)
                context["user_name"] = user_name
                context["message"] = message
                context["total_count"] = total_count
                context["projects"] = data
                context["page"] = page
                return render(request, "searchForm.html", context)

            message = "User not found. Check username"
            context["message"] = message
            return render(request, "index.html", context)
    else:
        message = "You submitted an empty form."
    context["message"] = message
    return render(request, "index.html", context)
