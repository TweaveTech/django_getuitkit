from django import template

register = template.Library()


def titleify_tag(obj):
    """
    returns the value for a field on the object
    Use like: {{ object|titleify }}
    """
    return obj.replace('_', ' ').title()


register.filter('titleify', titleify_tag)
