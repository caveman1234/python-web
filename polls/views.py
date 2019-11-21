from django.http import HttpResponse
from django.shortcuts import render
from django.http.response import JsonResponse

def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.<div style='color:red;'>dddd</div>")
    context = {}
    context['hello'] = 'hello'
    # return render(request,"test.html",context)
    return JsonResponse(context)
