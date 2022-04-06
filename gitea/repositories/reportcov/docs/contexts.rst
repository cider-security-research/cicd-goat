========
Contexts
========

Coverage.py 5.0 can record separate coverage data for `different contexts`_ during
one run of a test suite.  Pytest-cov can use this feature to record coverage
data for each test individually, with the ``--cov-context=test`` option.

.. _different contexts: https://coverage.readthedocs.io/en/stable/contexts.html

The context name recorded in the coverage.py database is the pytest test id,
and the phase of execution, one of "setup", "run", or "teardown".  These two
are separated with a pipe symbol.  You might see contexts like::

    test_functions.py::test_addition|run
    test_fancy.py::test_parametrized[1-101]|setup
    test_oldschool.py::RegressionTests::test_error|run

Note that parameterized tests include the values of the parameters in the test
id, and each set of parameter values is recorded as a separate test.

To view contexts when using ``--cov-report=html``, add this to your ``.coveragerc``::

    [html]
    show_contexts = True

The HTML report will include an annotation on each covered line, indicating the
number of contexts that executed the line. Clicking the annotation displays a
list of the contexts.
