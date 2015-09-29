# -*- coding: utf-8 -*-


def test_model(foo_proxy):
    assert foo_proxy[u'proxy'].proxied_object == foo_proxy[u'foo']
