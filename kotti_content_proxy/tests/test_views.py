# -*- coding: utf-8 -*-


def test_view_view(foo_proxy, webtest):

    foo = webtest.get('/foo')
    proxy = webtest.get('/proxy')
