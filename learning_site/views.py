from django.shortcuts import render

def hello_world(request):
    # return HttpResponse('Hello, World!')
    return render(request,'index.html')
