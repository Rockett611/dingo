from django.urls import path
from .views import math, math_operation, maths_list, math_details, results_list

# add, sub, mul, div,


app_name='maths'
urlpatterns = [
    path('', math),
    path('<operation>/<int:a>/<int:b>', math_operation),
    path('histories/', maths_list, name='list'),
    path('histories/<id>', math_details, name='details'),
    path('results/', results_list, name="results"),
]