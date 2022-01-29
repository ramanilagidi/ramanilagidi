from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request,'testapp/home.html')

def first_view(request):
    return render(request,'testapp/first.html')

def second_view(request):
    first= request.GET['p1']
    if len(first) <= 0 :
        return render(request,'testapp/first.html')
    else:
        response= render(request,'testapp/second.html')
        #response.set_cookie('p1',first)
    return response

def third_view(request):
    first = request.COOKIES['p1']
    second = request.GET['p2']
    #response =render(request,'testapp/third.html')
    #response.set_cookie('p1',first)
    #response.set_cookie('p2',second)
    return response

def result_view(request):
    first=request.COOKIES['p1']
    second = request.COOKIES['p2']
    third = request.GET['p3']


    return render(request,'testapp/result.html',{'p1':first,'p2':second,'p3':third})
