from django.contrib import admin

# Register your models here.
from product.models import Event


class EventAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "thumbnail", "description", "dt_created", "exposure_start_date", "exposure_end_date"]


admin.site.register(Event, EventAdmin)