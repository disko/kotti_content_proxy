# -*- coding: utf-8 -*-

import pytest


def test_model(foo_proxy):
    assert foo_proxy[u'proxy'].proxied_object == foo_proxy[u'foo']


def test_proxying_custom_attributes(foo_proxy):

    import kotti_content_proxy

    mock_settings = {
        'kotti.available_types': '',
        'pyramid.includes': '',
    }

    settings = {
        'kotti_content_proxy.proxied_attributes':
            'some_attribute another_attribute'
    }

    settings.update(mock_settings)

    kotti_content_proxy.kotti_configure(settings)

    foo = foo_proxy['foo']
    foo.some_attribute = u'some value'
    proxy = foo_proxy['proxy']

    assert proxy.some_attribute == foo.some_attribute
    with pytest.raises(AttributeError) as excinfo:
        proxy.another_attribute
    assert excinfo.value.args[0] == "'Document' object has no attribute 'another_attribute'"  # noqa
