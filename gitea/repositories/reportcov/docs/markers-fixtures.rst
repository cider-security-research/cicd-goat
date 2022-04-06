====================
Markers and fixtures
====================

There are some builtin markers and fixtures in ``pytest-cov``.

Markers
=======

``no_cover``
------------

Eg:

.. code-block:: python

    @pytest.mark.no_cover
    def test_foobar():
        # do some stuff that needs coverage disabled

.. warning:: Caveat

    Note that subprocess coverage will also be disabled.

Fixtures
========

``no_cover``
------------

Eg:

.. code-block:: python

    def test_foobar(no_cover):
        # same as the marker ...

``cov``
-------

For reasons that no one can remember there is a ``cov`` fixture that provides access to the underlying Coverage instance.
Some say this is a disguised foot-gun and should be removed, and some think mysteries make life more interesting and it should
be left alone.
