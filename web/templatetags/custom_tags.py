from django import template

register = template.Library()

@register.filter
def short_description(value, max_length=100):
    if len(value) > max_length:
        return value[:max_length] + "..."
    return value


@register.filter
def replace_char(value, replace_char="&nbsp;", with_char=" "):
    return str(value).replace(replace_char, with_char)