=====================
Debuggers and PyCharm
=====================

(or other IDEs)

When it comes to TDD one obviously would like to debug tests. Debuggers in Python use mostly the sys.settrace function
to gain access to context. Coverage uses the same technique to get access to the lines executed. Coverage does not play
well with other tracers simultaneously running. This manifests itself in behaviour that PyCharm might not hit a
breakpoint no matter what the user does. Since it is common practice to have coverage configuration in the pytest.ini
file and pytest does not support removeopts or similar the `--no-cov` flag can disable coverage completely.

At the reporting part a warning message will show on screen::

    Coverage disabled via --no-cov switch!
