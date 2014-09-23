# -*- coding: utf-8 -*-

"""
Created on 2014-09-23
:author: Andreas Kaiser (disko)
"""

from kotti.resources import Content
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer

from kotti_content_proxy import _


class ContentProxy(Content):
    """ A ContentProxy refers to any other content node in the site. """

    id = Column(
        Integer,
        ForeignKey('contents.id'),
        primary_key=True)
    proxied_id = Column(
        Integer,
        ForeignKey('contents.id'),
        nullable=False)

    type_info = Content.type_info.copy(
        name=u'ContentProxy',
        title=_(u'Content Type'),
        add_view=u'add_content_type',
        addable_to=[u'Document'],
        )

    def __init__(self, proxied_id=None, **kwargs):

        super(ContentProxy, self).__init__(**kwargs)
        self.proxied_id = proxied_id
