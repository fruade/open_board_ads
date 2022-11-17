from django import template

register = template.Library()


@register.filter(name='digit_cap')
def digit_capacity(val):
    n = str(val)[::-1]
    return ' '.join(n[i:i + 3] for i in range(0, len(n), 3))[::-1]

