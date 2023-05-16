from django.urls import path
from .views import math, math_operation
# add, sub, mul, div,

urlpatterns = [
    path('', math),
    path('<operation>/<int:a>/<int:b>', math_operation),
    # path('sub/<int:a>/<int:b>', sub),
    # path('mul/<int:a>/<int:b>', mul),
    # path('div/<int:a>/<int:b>', div),
]