# -*- coding: utf-8 -*-


def test_model(root, db_session):

    from kotti.resources import Document
    from kotti_content_proxy.resources import ContentProxy

    doc = Document.query.filter(Document.id == 2).one()

    # create a proxy for the "about" document
    root['proxy'] = ContentProxy(proxied_id=2, title="proxied about")
    db_session.flush()

    assert root['proxy'].proxied_object == doc
