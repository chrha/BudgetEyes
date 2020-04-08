from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login 
from django.contrib.auth.decorators import login_required
import json


from .forms import CurrencyForm, LoginForm
from .models import Currency


# Create your views here.


def index(request):
    return redirect("/example")

@login_required
def example(request):

    if request.method == "POST":
        print("Post")
        form = CurrencyForm()
        #if form.is_valid(): No longer working due to AJAX call instead of form action
        data = json.loads(request.body.decode('utf-8'))
        print(data)
        form = CurrencyForm()
        msg = ""
        try:
            c = Currency.objects.get(name=data.get("currency_name"))
            c.value = data.get("new_value")
            c.save()
            print("Saved")
            return HttpResponse("Saved")
        except Currency.DoesNotExist:
            print("Entry not found")
            msg = "Not saved"
            response = HttpResponse(msg)
            response.status_code = 400
            return response

        #else:
            #print("Not valid")
    else:
        form = CurrencyForm()

        currencies = Currency.objects.all()
        currdict = {k:v for (k,v) in [(x.name, x.value) for x in currencies]}

        return render(request, 'example.html', {"form":form, "currencies" : currdict})

def sign_in(request):
    if request.method == "POST":
        form = LoginForm(request.POST, auto_id=True)
        if form.is_valid():
            print("Got post")
            data = form.cleaned_data
            print(data)
            username = data.get("username")
            password = data.get("password")
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect("/example/")
            else:
                error_msg = "No user with those credentials"
                messages.error(request, error_msg)
    else:
        form = LoginForm(auto_id=True)

    return render(request, 'login.html', {"form" : form})