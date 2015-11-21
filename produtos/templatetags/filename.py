import os
from django import template

register = template.Library()

@register.filter
def filename(value):
    return os.path.basename(value.file.name)

@register.filter
def classname(value):
    return value.__class__.__name__

@register.filter
def index(List, i):
    return List[int(i)]