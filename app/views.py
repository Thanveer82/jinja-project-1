from django.shortcuts import render

# Create your views here.
def first(request):
    d={'name':'Thanveer','age':22}
    return render(request,'veer.html',context=d)
