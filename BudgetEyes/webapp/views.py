from django.shortcuts import render


# Create your views here.


def index(request):
    context = {
        'currencies' : [["USD", 10], ["CAD", 8], ["NOK", 1.5]]
    }
    return render(request, 'index.html', context=context)
