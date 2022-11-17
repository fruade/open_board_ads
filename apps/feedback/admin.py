from django.contrib import admin

from apps.feedback.models import FeedBack


class FeedBackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'user', 'rating', 'feedback')
    list_filter = ('email', 'user')
    list_display_links = ('name', 'email', 'user', 'feedback')


admin.site.register(FeedBack, FeedBackAdmin)
