# -*- coding: utf-8 -*-


def test_model(root, db_session, content):

    from kotti.resources import Document
    from kotti_content_proxy.resources import ContentProxy

    root[u'foo'] = Document(title=u'Foo')
    db_session.flush()

    doc = root[u'foo']

    # create a proxy for the document
    root['proxy'] = ContentProxy(proxied_id=doc.id, title="proxied about")
    db_session.flush()

    assert root['proxy'].proxied_object == doc
