# -*- coding: utf-8 -*-

"""
Created on 2014-09-23
:author: Andreas Kaiser (disko)
"""

import colander
from kotti.util import render_view
from kotti.views.edit import AddFormView
from kotti.views.edit import EditFormView
from pyramid.response import Response
from pyramid.view import view_config
from pyramid.view import view_defaults

from kotti_content_proxy import _
from kotti_content_proxy.resources import ContentProxy


class ContentProxySchema(colander.MappingSchema):
    title = colander.SchemaNode(
        colander.String(),
        title=_(u'Title'))
    proxied_id = colander.SchemaNode(
        colander.Integer(),
        title=_(u'Proxied ID'))


@view_config(name=ContentProxy.type_info.add_view,
             permission='add',
             renderer='kotti:templates/edit/node.pt')
class ContentProxyAddForm(AddFormView):
    schema_factory = ContentProxySchema
    add = ContentProxy
    item_type = _(u"ContentProxy")


@view_config(context=ContentProxy,
             name='edit',
             permission='edit',
             renderer='kotti:templates/edit/node.pt')
class ContentProxyEditForm(EditFormView):
    schema_factory = ContentProxySchema


@view_defaults(context=ContentProxy, permission='view')
class ContentProxyView(object):
    """docstring for ContentProxyView"""

    def __init__(self, context, request):
        super(ContentProxyView, self).__init__()
        self.context = context
        self.request = request

    @view_config(name='view')
    def view(self):
        return Response(render_view(
            self.context.proxied_object,
            self.request,
            name='view',
            secure=True))
