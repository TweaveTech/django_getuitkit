from django import template

register = template.Library()


def getattr_tag(obj, f):
    """
    returns the value for a field on the object
    Use like: {{ object|getattr:field }}
    """
    return getattr(obj, f)


register.filter('getattr', getattr_tag)
