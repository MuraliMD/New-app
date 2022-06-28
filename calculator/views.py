from pickle import FALSE
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request,"calculator/form.html")

def cal(request):
    sub1=int(request.GET["sub1"])
    sub2=int(request.GET["sub2"])
    sub3=int(request.GET["sub3"])
    sub4=int(request.GET["sub4"])
    sub5=int(request.GET["sub5"])
    sub6=int(request.GET["sub6"])
    
    lab1=int(request.GET["lab1"])
    lab2=int(request.GET["lab2"])
    lab3=int(request.GET["lab3"])



    sub7=int(request.GET['sub7'])
    sub8=int(request.GET["sub8"])
    sub9=int(request.GET["sub9"])
    sub10=int(request.GET["sub10"])
    sub11=int(request.GET["sub11"])
    sub12=int(request.GET["sub12"])

    lab4=int(request.GET["lab4"])
    lab5=int(request.GET["lab5"])
    lab6=int(request.GET["lab6"])



    sub13=int(request.GET["sub13"])
    sub14=int(request.GET["sub14"])
    sub15=int(request.GET["sub15"])
    sub16=int(request.GET["sub16"])
    sub17=int(request.GET["sub17"])
    sub18=int(request.GET["sub18"])
    
    lab7=int(request.GET["lab7"])
    lab8=int(request.GET["lab8"])
    lab9=int(request.GET["lab9"])


   
    sub19=int(request.GET["sub19"])
    sub20=int(request.GET["sub20"])
    sub21=int(request.GET["sub21"])
    sub22=int(request.GET["sub22"])
    sub23=int(request.GET["sub23"])
    sub24=int(request.GET["sub24"])

    lab10=int(request.GET["lab10"])
    lab11=int(request.GET["lab11"])
    lab12=int(request.GET["lab12"])



    sub25=int(request.GET["sub25"])
    sub26=int(request.GET["sub26"])
    sub27=int(request.GET["sub27"])
    sub28=int(request.GET["sub28"])
    sub29=int(request.GET["sub29"])
    sub30=int(request.GET["sub30"])

    lab13=int(request.GET["lab13"])
    lab14=int(request.GET["lab14"])
    lab15=int(request.GET["lab15"])


    GP=int(request.GET["GP"])

    
    res1 = sub1*4+sub2*4+sub3*4+sub4*4+sub5*4+sub6*4+lab1*2+lab2*2+lab3*2
    res2 = sub7*4+sub8*4+sub9*4+sub10*4+sub11*4+sub12*4+lab4*2+lab5*2+lab6*2
    res3 = sub13*4+sub14*4+sub15*4+sub16*4+sub17*4+sub18*4+lab7*2+lab8*2+lab9*2
    res4 = sub19*4+sub20*4+sub21*4+sub22*4+sub23*4+sub24*4+lab10*2+lab11*2+lab12*2
    res5 = sub25*4+sub26*4+sub27*4+sub28*4+sub29*4+sub30*4+lab13*2+lab14*2+lab15*2+GP
    res= res1+res2+res3+res4+res5
    total= res/150
    percentage= (total - 0.5)*10
    return render(request,"calculator/result1.html", {"result":total})
    