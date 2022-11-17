from django.contrib import admin
from django.contrib.admin import display
from related_admin import RelatedFieldAdmin, getter_for_related_field

from apps.ads.models import Card, CardPhoto


class CardPhotoAdmin(admin.ModelAdmin):
    pass


class CardPhotoInline(admin.StackedInline):
    model = CardPhoto
    max_num = 6
    extra = 0


class CardAdmin(RelatedFieldAdmin):
    # photos__card_img = getter_for_related_field('photos__card_img', short_description='Фотографии', boolean=True)
    inlines = [CardPhotoInline, ]
    list_display = ('id', 'title', 'slug', 'price', 'id_category', 'id_user', 'condition',
                    'date_add', 'is_deleted')
    list_editable = ('is_deleted',)
    list_display_links = ('id', 'title', 'slug')
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ('id', 'title', 'slug', 'price', 'id_category', 'id_user', 'condition', 'description',
                     'date_add', 'is_deleted')
    list_filter = ('price', 'id_category', 'id_user', 'condition', 'description',
                   'date_add')


admin.site.register(Card, CardAdmin)
admin.site.register(CardPhoto, CardPhotoAdmin)