=========
Releasing
=========

The process for releasing should follow these steps:

#. Test that docs build and render properly by running ``tox -e docs,spell``.

   If there are bogus spelling issues add the words in ``spelling_wordlist.txt``.
#. Update ``CHANGELOG.rst`` and ``AUTHORS.rst`` to be up to date.
#. Bump the version by running ``bumpversion [ major | minor | patch ]``. This will automatically add a tag.

   Alternatively, you can manually edit the files and run ``git tag v1.2.3`` yourself.
#. Push changes and tags with::

    git push
    git push --tags
#. Wait for `AppVeyor <https://ci.appveyor.com/project/pytestbot/pytest-cov>`_
   and `GitHub Actions <https://github.com/pytest-dev/pytest-cov/actions>`_ to give the green builds.
#. Check that the docs on `ReadTheDocs <https://readthedocs.org/projects/pytest-cov>`_ are built.
#. Make sure you have a clean checkout, run ``git status`` to verify.
#. Manually clean temporary files (that are ignored and won't show up in ``git status``)::

        rm -rf dist build src/*.egg-info

   These files need to be removed to force distutils/setuptools to rebuild everything and recreate the egg-info metadata.
#. Build the dists::

        python3 setup.py clean --all sdist bdist_wheel

#. Verify that the resulting archives (found in ``dist/``) are good.
#. Upload the sdist and wheel with twine::

    twine upload dist/*
