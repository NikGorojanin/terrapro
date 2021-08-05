from django import template
import ast
import logging

register = template.Library()

logger = logging.getLogger(__name__)


@register.filter(name='html_attrs')
def html_attrs(value, attrs):
    attrs = ast.literal_eval('{{{0}}}'.format(attrs))

    if hasattr(value, "field"):
        value.field.widget.attrs.update(attrs)

    return str(value)
