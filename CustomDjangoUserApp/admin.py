from django.contrib import admin
from django.contrib.auth import get_user_model

from .forms import AdminChangeForm, AdminCreationForm

User = get_user_model()

class UserAdmin(admin.ModelAdmin):

    form = AdminChangeForm
    add_form = AdminCreationForm

    search_fields = [
        'email'
    ]

    class Meta:
        model = User

admin.site.register(User, UserAdmin)