from django import template
from reviews.models import QUALITY_MAPPING

register = template.Library()

@register.filter
def quality_grade(value):
    return QUALITY_MAPPING.get(value, value)