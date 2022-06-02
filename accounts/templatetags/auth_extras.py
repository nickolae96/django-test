from django import template
from django.contrib.auth.models import Group

register = template.Library()


@register.filter(name='has_group')
def has_group(user, group_name): 
    group = Group.objects.get(name=group_name)
    in_group = False
    if group in user.groups.all():
        in_group = True
    return in_group
