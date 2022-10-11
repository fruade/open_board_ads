from django.contrib import admin
from apps.categories.models import Category
from django_mptt_admin.admin import DjangoMpttAdmin


class CategoryAdmin(DjangoMpttAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('id', 'title', 'cat_img')
    list_display_links = ('id', 'title', )
    search_fields = ('title',)
    list_editable = ('cat_img',)


admin.site.register(Category, CategoryAdmin)
