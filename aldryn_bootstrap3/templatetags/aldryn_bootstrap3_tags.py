# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import
from django import template
from django.template.defaultfilters import stringfilter
from classytags.core import Tag, Options
from classytags.arguments import Argument, MultiKeywordArgument


register = template.Library()


@register.filter(name='iconset_from_class')
@stringfilter
def iconset_from_class(value):
    """
    extracts the iconset from a class definition
    "fa-flask" -> "fa"
    :param value:
    :return:
    """
    if '-' in value:
        return value.split('-')[0]
    return ''


class ColumnContext(Tag):
    name = 'aldryn_bootstrap3_column_context'
    options = Options(
        MultiKeywordArgument('column'),
        blocks=[('end_aldryn_bootstrap3_column_context', 'nodelist')],
    )

    def render_tag(self, context, variable, varname, nodelist):
        context.push()
        context[varname] = variable
        output = nodelist.render(context)
        context.pop()
        return output

register.tag(ColumnContext)
