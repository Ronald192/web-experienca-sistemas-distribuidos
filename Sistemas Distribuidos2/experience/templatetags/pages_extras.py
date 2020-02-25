from django import template
from experience.models import Experience

register = template.Library()

@register.simple_tag
def get_experience_list():
    experience = Experience.objects.all()
    return experience