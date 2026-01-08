from django.contrib import admin
from .models import Bakery

# Register your models here.
# admin.site.register(Bakery)

@admin.register(Bakery)
class BakeryAdmin(admin.ModelAdmin):
    list_display = ('name', 'rating')