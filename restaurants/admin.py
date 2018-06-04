from django.contrib import admin

from .models import Restaurant


class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'opens_at', 'closes_at')


admin.site.register(Restaurant, RestaurantAdmin)
