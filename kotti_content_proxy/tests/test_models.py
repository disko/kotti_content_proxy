# -*- coding: utf-8 -*-


def test_model(root, foo_proxy):
    assert root['proxy'].proxied_object == root[u'foo']
