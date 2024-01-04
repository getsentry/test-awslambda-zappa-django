from django.http import HttpResponse

def error(request):
    1/0
    return HttpResponse("This should raise an errror!")
                        
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")