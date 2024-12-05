from django.shortcuts import render

# Create your views here.

def condition1(request):
    d={'name':'Kishore','a':7}
    return render(request,'if.html',context=d)