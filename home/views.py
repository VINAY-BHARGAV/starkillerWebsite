from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    #return HttpResponse("this is home page")
    return render(request, 'index.html')
def about(request):
    #return HttpResponse("this is about page")
    return render(request, 'aboutme.html')
def qualification(request):
    return render(request, 'qualification.html')
def contact(request):
    return render(request, 'contact.html')
def faverate(request):
    return render(request, 'faverate.html')
