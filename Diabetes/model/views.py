from django.http.response import HttpResponse
from django.shortcuts import redirect, render
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn import linear_model
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.


def front(request):
     if request.user.is_authenticated:
        return redirect('predictd')
     else:
        return render(request,'front.html')

@login_required(login_url='login')
def predict(request):
    return render(request,"predict.html")


def result(request):
    data = pd.read_csv("diabetes.csv")
    X=data.drop("Outcome",axis=1)
    Y=data['Outcome']
    X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2)
    model=LogisticRegression()
    model.fit(X_train,Y_train)

    value1= float(request.GET['n1'])
    value2= float(request.GET['n2'])
    value3= float(request.GET['n3'])
    value4= float(request.GET['n4'])
    value5= float(request.GET['n5'])
    value6= float(request.GET['n6'])
    value7= float(request.GET['n7'])
    value8= float(request.GET['n8'])
    
 
    pred=model.predict([[value1,value2,value3,value4,value5,value6,value7,value8]])

    ResultCame=""

        

    if pred==[1]:
            ResultCame="Positive"
    else:
            ResultCame="Negative"

    return render(request,"predict.html",{"ResultCame":ResultCame})


def reg(request):
    form=CreateUserForm()
    if request.user.is_authenticated:
        return redirect('predictd')
    else:
        if request.method == 'POST':
            form= CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user= form.cleaned_data.get('username')
                messages.success(request,"Account was created for"+ user)
                return redirect('login')
        
        return render(request,"register.html",{"form":form})

def mylogin(request):
     if request.user.is_authenticated:
        return redirect('predictd')
     else:

        if request.method == "POST":
            username=request.POST.get('username')
            password=request.POST.get('password')

            user=authenticate(request,username=username,password=password)

            if user is not None:
                login(request,user)
                return redirect('predictd')
            else:
                messages.info(request,"Username or Password is incorrect")
        context={}       
        return render(request,'login.html',context)


def logoutUser(request):
    logout(request)
    return redirect('login')


def about(request):
    return render(request,'about.html')

