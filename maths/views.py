from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import loader, Context


def math(request):
    return HttpResponse("Tu będzie matma")


def add(request, a, b):
    a, b = int(a), int(b)
    wynik = a + b
    c = {"a":a, "b":b, "operacja": "+", "wynik": wynik}
    return render(request, "maths/main.html", c)


def sub(request, a, b):
    # a, b = int(a), int(b)
    c = {"a": int(a), "b": int(b), "operacja": "-", "wynik": int(a)-int(b)}
    return render(request, "maths/main.html", c)


def mul(request, a, b):
    c = {"a": int(a), "b": int(b), "operacja": "*", "wynik": int(a)*int(b)}
    return render(request, "maths/main.html", c)


def div(request, a, b):
    c = {"a": int(a), "b": int(b), "operacja": ":", "wynik": "0"}
    if int(b) == 0:
        c["wynik"] = "żal i cierpienie, bo nie pamiętałeś, że przez 0 się nie dzieli"
    else:
        c["wynik"] = int(a) / int(b)

    return render(request, "maths/main.html", c)