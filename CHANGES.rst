Changelog
=========

0.4.1 - unreleased
------------------

- No changes yet.

0.4.0 - 2015-10-07
------------------

- Now we take object to be proxied instead of its id.
  **This is a backward incompatible change.**

0.3.0 - 2015-10-05
------------------

- Names of proxied attributes are now kept in class attribute and read from
  ``kotti_content_proxy.proxied_attributes`` setting.

0.2.0 - 2015-09-30
------------------

- Proxy now declares unique ``polymorphic_identity`` for use in SQLAlchemy.
- Added proxying of custom attributes.

0.1.0
-----

- Initial release.
