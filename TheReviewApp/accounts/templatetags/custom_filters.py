from django import template

register = template.Library()
MAX_DESCRIPTION_LENGTH = 50


@register.filter
def short_description(value: str):
    result = value
    if len(value) > MAX_DESCRIPTION_LENGTH:
        result = value[:MAX_DESCRIPTION_LENGTH] + "..."
    return result
