========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |github-actions| |appveyor| |requires|
    * - package
      - | |version| |conda-forge| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|

.. |docs| image:: https://readthedocs.org/projects/pytest-cov/badge/?style=flat
    :target: https://readthedocs.org/projects/pytest-cov
    :alt: Documentation Status

.. |github-actions| image:: https://github.com/pytest-dev/pytest-cov/actions/workflows/test.yml/badge.svg
    :alt: GitHub Actions Status
    :target: https://github.com/pytest-dev/pytest-cov/actions

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/pytest-dev/pytest-cov?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/pytestbot/pytest-cov

.. |requires| image:: https://requires.io/github/pytest-dev/pytest-cov/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/pytest-dev/pytest-cov/requirements/?branch=master

.. |version| image:: https://img.shields.io/pypi/v/pytest-cov.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/pytest-cov

.. |conda-forge| image:: https://img.shields.io/conda/vn/conda-forge/pytest-cov.svg
    :target: https://anaconda.org/conda-forge/pytest-cov

.. |commits-since| image:: https://img.shields.io/github/commits-since/pytest-dev/pytest-cov/v3.0.0.svg
    :alt: Commits since latest release
    :target: https://github.com/pytest-dev/pytest-cov/compare/v3.0.0...master

.. |wheel| image:: https://img.shields.io/pypi/wheel/pytest-cov.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/pytest-cov

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/pytest-cov.svg
    :alt: Supported versions
    :target: https://pypi.org/project/pytest-cov

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/pytest-cov.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/pytest-cov

.. end-badges

This plugin produces coverage reports. Compared to just using ``coverage run`` this plugin does some extras:

* Subprocess support: you can fork or run stuff in a subprocess and will get covered without any fuss.
* Xdist support: you can use all of pytest-xdist's features and still get coverage.
* Consistent pytest behavior. If you run ``coverage run -m pytest`` you will have slightly different ``sys.path`` (CWD will be
  in it, unlike when running ``pytest``).

All features offered by the coverage package should work, either through pytest-cov's command line options or
through coverage's config file.

* Free software: MIT license

Installation
============

Install with pip::

    pip install pytest-cov

For distributed testing support install pytest-xdist::

    pip install pytest-xdist

Upgrading from ancient pytest-cov
---------------------------------

`pytest-cov 2.0` is using a new ``.pth`` file (``pytest-cov.pth``). You may want to manually remove the older
``init_cov_core.pth`` from site-packages as it's not automatically removed.

Uninstalling
------------

Uninstall with pip::

    pip uninstall pytest-cov

Under certain scenarios a stray ``.pth`` file may be left around in site-packages.

* `pytest-cov 2.0` may leave a ``pytest-cov.pth`` if you installed without wheels
  (``easy_install``, ``setup.py install`` etc).
* `pytest-cov 1.8 or older` will leave a ``init_cov_core.pth``.

Usage
=====

::

    pytest --cov=myproj tests/

Would produce a report like::

    -------------------- coverage: ... ---------------------
    Name                 Stmts   Miss  Cover
    ----------------------------------------
    myproj/__init__          2      0   100%
    myproj/myproj          257     13    94%
    myproj/feature4286      94      7    92%
    ----------------------------------------
    TOTAL                  353     20    94%

Documentation
=============

    http://pytest-cov.rtfd.org/






Coverage Data File
==================

The data file is erased at the beginning of testing to ensure clean data for each test run. If you
need to combine the coverage of several test runs you can use the ``--cov-append`` option to append
this coverage data to coverage data from previous test runs.

The data file is left at the end of testing so that it is possible to use normal coverage tools to
examine it.

Limitations
===========

For distributed testing the workers must have the pytest-cov package installed.  This is needed since
the plugin must be registered through setuptools for pytest to start the plugin on the
worker.

For subprocess measurement environment variables must make it from the main process to the
subprocess.  The python used by the subprocess must have pytest-cov installed.  The subprocess must
do normal site initialisation so that the environment variables can be detected and coverage
started.


Acknowledgements
================

Whilst this plugin has been built fresh from the ground up it has been influenced by the work done
on pytest-coverage (Ross Lawley, James Mills, Holger Krekel) and nose-cover (Jason Pellerin) which are
other coverage plugins.

Ned Batchelder for coverage and its ability to combine the coverage results of parallel runs.

Holger Krekel for pytest with its distributed testing support.

Jason Pellerin for nose.

Michael Foord for unittest2.

No doubt others have contributed to these tools as well.
