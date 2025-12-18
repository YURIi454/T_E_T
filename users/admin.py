from django.contrib import admin

from users.models import CustomUser


@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    """ Отображение юзера в админке. """

    list_filter = ("name", "email")
