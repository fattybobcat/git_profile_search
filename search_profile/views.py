from django.shortcuts import render
import requests
# Create your views here.
def api_s(request, user):
    addr = 'https://api.github.com/users/' + user
    r = requests.get(addr)
    print(addr)
    print(r.content)
    print(r.status_code)
    return r.content
def index(request):
    context = {}
    return render(request, 'index.html', context)


def search(request):
    context = {}
    print("request", request.GET['q'])
    print("request.method", request.method )
    if 'q' in request.GET:
        message = 'You searched for: %r' % request.GET['q']
        user_name = request.GET['q']
        data = api_s(request, user_name)
        context['data'] = data
    else:
        message = 'You submitted an empty form.'
    context["message"] = message
    return render(request, 'index.html', context)