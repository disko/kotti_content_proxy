# -*- coding: utf-8 -*-

"""
Created on 2014-09-23
:author: Andreas Kaiser (disko)
"""

import colander
from kotti.views.edit import AddFormView
from kotti.views.edit import ContentSchema
from kotti.views.edit import EditFormView
from pyramid.config import view_config
from pyramid.config import view_defaults

from kotti_content_proxy import _
from kotti_content_proxy.resources import ContentProxy


class ContentProxySchema(ContentSchema):
    example_text = colander.SchemaNode(colander.String())


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

    @view_config(name='view', renderer='templates/view.pt')
    def view(self):
        return {
        }
