# -*- coding: utf-8 -*-

"""
Created on 2014-09-23
:author: Andreas Kaiser (disko)
"""

from kotti.resources import Content
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy.orm import relationship

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

    proxied_object = relationship(Content, foreign_keys=[proxied_id])

    # This can't be None as __getattribute__ is being called by SQLAlchemy's
    # instrumentation before __init__ is called. See
    # sqlalchemy.orm.instrumentation.ClassManager._new_state_if_none()
    proxied_attrs = set()
    _default_proxied_attrs = set(('__acl__',))

    __mapper_args__ = Content.__mapper_args__.copy()
    __mapper_args__.update({
        'inherit_condition': (id == Content.id),
        'polymorphic_identity': 'content_proxy',
    })

    type_info = Content.type_info.copy(
        name=u'ContentProxy',
        title=_(u'Content Proxy'),
        add_view=u'add_content_proxy',
        addable_to=[u'Document'],
        )

    def __init__(self, proxied_id=None, proxied_attrs=None, **kwargs):
        """ Constructor

        :param proxied_id: id of the proxied object
        :type proxied_id: int

        :param **kwargs: see :class:`kotti.resources.Content`
        :type **kwargs: variant
        """

        super(ContentProxy, self).__init__(**kwargs)
        self.proxied_id = proxied_id

    def __getattribute__(self, key):
        """ Proxy some attributes.
            See https://www.inkling.com/read/learning-python-mark-lutz-4th/chapter-37/--getattr---and---getattribute--  # noqa
        """
        super_getattribute = super(ContentProxy, self).__getattribute__
        proxied_attrs = super_getattribute('proxied_attrs')

        if key in proxied_attrs:
            return self.proxied_object.__getattribute__(key)

        return super(ContentProxy, self).__getattribute__(key)
