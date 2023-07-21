from django import template
register = template.Library()


def firstFilter(value, s):
    m, n = [int(i) for i in s.split(',')]
    result = value[m:n].lower()
    return result
register.filter('ffu', firstFilter)