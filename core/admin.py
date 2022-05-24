from django.contrib import admin
from .models import *
from .forms import *

class CustomUserAdmin(admin.ModelAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ['username', 'email']

admin.site.register(CustomUser, CustomUserAdmin)