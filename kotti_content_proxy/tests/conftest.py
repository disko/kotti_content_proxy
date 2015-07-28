# -*- coding: utf-8 -*-

from pytest import fixture

pytest_plugins = "kotti"


@fixture
def foo_proxy(root, db_session, content):

    from kotti.resources import Document
    from kotti_content_proxy.resources import ContentProxy

    root[u'foo'] = Document(title=u'Foo', description=u'Bar',
                            body=u'This is the Foo document')
    db_session.flush()

    doc = root[u'foo']

    # create a proxy for the document
    root['proxy'] = ContentProxy(proxied_id=doc.id, title=u'Proxy',
                                 description=u'This is a proxy')
    db_session.flush()
