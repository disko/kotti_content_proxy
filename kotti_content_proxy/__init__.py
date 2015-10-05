# -*- coding: utf-8 -*-

"""
Created on 2014-09-23
:author: Andreas Kaiser (disko)
"""

from pyramid.i18n import TranslationStringFactory

_ = TranslationStringFactory('kotti_content_proxy')


def includeme(config):
    config.scan()


def kotti_configure(settings):
    settings['pyramid.includes'] += ' kotti_content_proxy'
    settings['kotti.available_types'] += ' kotti_content_proxy.resources.ContentProxy'  # noqa

    proxied_attrs = settings.get('kotti_content_proxy.proxied_attributes', '')
    proxied_attrs = set(proxied_attrs.split())

    from .resources import ContentProxy

    ContentProxy.proxied_attrs = \
        ContentProxy._default_proxied_attrs | proxied_attrs
