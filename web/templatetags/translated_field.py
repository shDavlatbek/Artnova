from django import template
from django.utils.translation import get_language

register = template.Library()

@register.filter
def translated_field(instance, field_name):
    current_language = get_language()
    full_field_name = f"{field_name}_{current_language}"
    return getattr(instance, full_field_name, "")