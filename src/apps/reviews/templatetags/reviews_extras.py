from django import template

register = template.Library()

@register.filter
def model_type(instance):
    return type(instance).__name__
