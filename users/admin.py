from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'first_name', 'last_name', 'email', 'date_joined', )
    list_filter = ('date_joined',)
    search_fields = ('username',)
    date_hierarchy = 'date_joined'
