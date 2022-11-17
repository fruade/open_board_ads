from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def max_file_size(value):
    maximum = 5
    limit = maximum * 1024 * 1024
    if value.size > limit:
        raise ValidationError(f'Размер фото не должен превышать {maximum} мб')

