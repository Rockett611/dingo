from django.contrib import admin

from maths.models import Math, Result

# Register your models here.


class MathAdmin(admin.ModelAdmin):
    list_display = ['id', 'operation', 'a', 'b', 'created', 'result'] #lista kolumn widoczna w panelu adm
    list_filter = ['operation'] #filtry w panelu bocznym
    search_fields = ['a', 'b'] #dodaje pole wyszukiwania po wybranych


admin.site.register(Math, MathAdmin)


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ['id', 'value', 'error']
