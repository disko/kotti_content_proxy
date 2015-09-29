# -*- coding: utf-8 -*-

from pytest import fixture

pytest_plugins = "kotti"


@fixture
def foo_proxy(root, db_session, content):

    from kotti.resources import Document
    from kotti_content_proxy.resources import ContentProxy

    foo = root[u'foo'] = Document(title=u'Foo', description=u'Bar',
                                  body=u'This is the Foo document')
    db_session.flush()

    # create a proxy for the 'foo'
    proxy = root[u'proxy'] = ContentProxy(proxied_id=foo.id, title=u'Proxy',
                                          description=u'This is a proxy')
    db_session.flush()

    return dict(
        foo=foo,
        proxy=proxy,
    )
