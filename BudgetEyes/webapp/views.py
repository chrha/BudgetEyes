from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
import json


from .forms import CurrencyForm, LoginForm
from .models import Currency


# Create your views here.


def index(request):
    return redirect("/example")


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

def login(request):
    form = LoginForm(request.POST, auto_id=True)

    if request.method == "POST":
        if form.is_valid():
            print("Got post")
            data = form.cleaned_data
            print(data)
            messages.success(request, 'Post received')
        else:
            error_msg = form.errors.get("__all__")[0]
            messages.error(request, error_msg)

    return render(request, 'login.html', {"form" : form})