from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader, Context

from .calculator import Calculator
from .forms import ResultForm
from .models import Math, Result


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


def math_operation(request, operation, a, b):
    calc = Calculator(operation, a, b)
    result = Result.objects.get_or_create(value=calc.operation_type()[operation]['math'])[0]
    Math.objects.create(operation=operation, a=a, b=b, result=result)
    return render(request, "maths/operations.html", {"data": calc})


@login_required
def maths_list(request):
    if request.method == "GET":
        maths = Math.objects.all()
        paginator = Paginator(maths, 5)
        page_number = request.GET.get('page')
        maths = paginator.get_page(page_number)
    elif request.method == "POST":
        operation = request.POST['operation']
        maths = Math.objects.filter(operation=operation)
        paginator = Paginator(maths, 5)
        page_number = request.GET.get('page')
        maths = paginator.get_page(page_number)



    return render(
        request=request,
        template_name="maths/list.html",
        context={"maths": maths}
    )


def math_details(request, id):
    math = Math.objects.get(id=id)
    return render(
        request=request,
        template_name="maths/details.html",
        context={"math": math}
    )


def results_list(request):
    if request.method == "POST":
        form = ResultForm(data=request.POST)

        if form.is_valid():
            if form.cleaned_data['error'] == '':
                form.cleaned_data['error'] = None
            form.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                "Utworzono nowy Result!!"
            )
        else:
            messages.add_message(
                request,
                messages.ERROR,
                form.errors['__all__']
            )

    form = ResultForm()
    results = Result.objects.all()
    return render(
        request=request,
        template_name="maths/results.html",
        context={
            "results": results,
            "form": form
        }
    )
