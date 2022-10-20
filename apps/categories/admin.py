from django.contrib import admin
from apps.categories.models import Category, Card, CardPhoto
from django_mptt_admin.admin import DjangoMpttAdmin


class CategoryAdmin(DjangoMpttAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('id', 'title', 'cat_img')
    list_display_links = ('id', 'title',)
    search_fields = ('title',)
    list_editable = ('cat_img',)


class CardPhotoAdmin(admin.ModelAdmin):
    pass


class CardPhotoInline(admin.StackedInline):
    model = CardPhoto
    max_num = 6
    extra = 0


class CardAdmin(admin.ModelAdmin):
    inlines = [CardPhotoInline, ]
    list_display = ('id', 'title', 'slug', 'price', 'id_category', 'id_user', 'condition', 'description',
                    'date_add', 'is_deleted')
    list_editable = ('is_deleted',)
    list_display_links = ('id', 'title', 'slug')
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ('id', 'title', 'slug', 'price', 'id_category', 'id_user', 'condition', 'description',
                     'date_add', 'is_deleted')
    list_filter = ('price', 'id_category', 'id_user', 'condition', 'description',
                   'date_add')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Card, CardAdmin)
admin.site.register(CardPhoto, CardPhotoAdmin)
