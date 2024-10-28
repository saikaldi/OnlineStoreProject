from django.contrib import admin
from .models import UserSubmission

@admin.register(UserSubmission)
class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone_number', 'email', 'comment', 'attached_file', 'agreement')
    verbose_name = "Пользователь"
    verbose_name_plural = "Пользователи"


