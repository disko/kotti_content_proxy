# -*- coding: utf-8 -*-


def test_model(root, foo_proxy):
    assert root[u'proxy'].proxied_object == root[u'foo']
