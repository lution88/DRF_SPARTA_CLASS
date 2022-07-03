from django.contrib import admin

# Register your models here.
from django.utils.safestring import mark_safe

from product.models import Event


class EventAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "title",
        # "thumbnail",
        "description",
        "dt_created",
        "exposure_start_date",
        "exposure_end_date",
        "is_active",
        "thumbnail_preview"
    ]
    list_display_links = [
        "id",
        "title",
        "description",
        "thumbnail_preview"
    ]

    def thumbnail_preview(self, obj):
        return mark_safe(f'<img src="/product/thumbnail/{obj.id}/" height="100px"/>')

    thumbnail_preview.short_description = "Thumbnail"


admin.site.register(Event, EventAdmin)