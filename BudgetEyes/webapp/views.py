from django.shortcuts import render
from .forms import CurrencyForm
from .models import Currency


# Create your views here.


def index(request):

    if request.method == "POST":
        print("Post")
        form = CurrencyForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            form = CurrencyForm()
            try:
                c = Currency.objects.get(name=data.get("currency_name"))
                c.value = data.get("new_value")
                c.save()
            except Currency.DoesNotExist:
                print("Entry not found")
        else:
            print("Not valid")
    else:
        form = CurrencyForm()

    currencies = Currency.objects.all()
    currlist = [[x.name, x.value] for x in currencies]
    print(currlist)    

    return render(request, 'index.html', {"form":form, "currencies" : currlist})
