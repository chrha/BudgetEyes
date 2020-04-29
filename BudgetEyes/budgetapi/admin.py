from django.contrib import admin
from .models import Budget, Stock, Profile

# Register your models here.

admin.site.register(Budget)
admin.site.register(Stock)
admin.site.register(Profile)
