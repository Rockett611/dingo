from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader, Context

from .calculator import Calculator


def math(request):
    return render(request, "maths/main.html", {})

"""
def add(request, a, b):
    a, b = int(a), int(b)
    wynik = a + b
    c = {"a": a, "b": b, "operacja": "+", "wynik": wynik, "title": "dodawanie"}
    return render(request, "maths/operations.html", c)


def sub(request, a, b):
    # a, b = int(a), int(b)
    c = {"a": int(a), "b": int(b), "operacja": "-", "wynik": int(a) - int(b), "title": "dodawanie"}
    return render(request, "maths/operations.html", c)


def mul(request, a, b):
    c = {"a": int(a), "b": int(b), "operacja": "*", "wynik": int(a) * int(b), "title": "dodawanie"}
    return render(request, "maths/operations.html", c)


def div(request, a, b):
    c = {"a": int(a), "b": int(b), "operacja": ":", "wynik": "0", "title": "dodawanie"}
    if int(b) == 0:
        c["wynik"] = "żal i cierpienie, bo nie pamiętałeś, że przez 0 się nie dzieli"
    else:
        c["wynik"] = int(a) / int(b)

    return render(request, "maths/operations.html", c)
"""
def math_operation(request ,operation, a, b):
    calc = Calculator(operation, a, b)
    return render(request, "maths/operations.html", {"data": calc})
