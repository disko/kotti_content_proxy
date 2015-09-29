# -*- coding: utf-8 -*-

import pytest


def test_model(foo_proxy):
    assert foo_proxy[u'proxy'].proxied_object == foo_proxy[u'foo']


def test_proxying_custom_attributes(root, db_session):
    from kotti.resources import Document
    from kotti_content_proxy.resources import ContentProxy

    foo = root[u'foo'] = \
        Document(
            title=u'Foo',
            description=u'Bar',
            body=u'This is the Foo document')
    foo.some_attribute = u'some value'
    db_session.flush()

    # create a proxy for the 'foo'
    proxy = root[u'proxy'] = \
        ContentProxy(
            proxied_id=foo.id,
            proxied_attrs=['some_attribute', 'another_attribute'],
            title=u'Proxy',
            description=u'This is a proxy')
    db_session.flush()

    assert proxy.some_attribute == foo.some_attribute
    with pytest.raises(AttributeError) as excinfo:
        proxy.another_attribute
    assert excinfo.value.message == "'Document' object has no attribute " \
                                    "'another_attribute'"
