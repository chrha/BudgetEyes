from django.shortcuts import render
from django.http import HttpResponse
import json


from .forms import CurrencyForm
from .models import Currency


# Create your views here.


def index(request):

    if request.method == "POST":
        print("Post")
        form = CurrencyForm(request.POST)
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
        print(currencies)
        currdict = {k:v for (k,v) in [(x.name, x.value) for x in currencies]}
        print(currdict)    

        return render(request, 'index.html', {"form":form, "currencies" : currdict})
