#!/usr/bin/env python

import os
import subprocess
import sys
from collections import defaultdict
from os.path import abspath
from os.path import dirname
from os.path import exists
from os.path import join

base_path = dirname(dirname(abspath(__file__)))


def check_call(args):
    print("+", *args)
    subprocess.check_call(args)


def exec_in_env():
    env_path = join(base_path, ".tox", "bootstrap")
    if sys.platform == "win32":
        bin_path = join(env_path, "Scripts")
    else:
        bin_path = join(env_path, "bin")
    if not exists(env_path):
        import subprocess

        print(f"Making bootstrap env in: {env_path} ...")
        try:
            check_call([sys.executable, "-m", "venv", env_path])
        except subprocess.CalledProcessError:
            try:
                check_call([sys.executable, "-m", "virtualenv", env_path])
            except subprocess.CalledProcessError:
                check_call(["virtualenv", env_path])
        print("Installing `jinja2` into bootstrap environment...")
        check_call([join(bin_path, "pip"), "install", "jinja2", "tox"])
    python_executable = join(bin_path, "python")
    if not os.path.exists(python_executable):
        python_executable += '.exe'

    print(f"Re-executing with: {python_executable}")
    print("+ exec", python_executable, __file__, "--no-env")
    os.execv(python_executable, [python_executable, __file__, "--no-env"])


def main():
    import jinja2

    print(f"Project path: {base_path}")

    jinja = jinja2.Environment(
        loader=jinja2.FileSystemLoader(join(base_path, "ci", "templates")),
        trim_blocks=True,
        lstrip_blocks=True,
        keep_trailing_newline=True
    )

    tox_environments = [
        line.strip()
        # WARNING: 'tox' must be installed globally or in the project's virtualenv
        for line in subprocess.check_output(['tox', '--listenvs'], universal_newlines=True).splitlines()
    ]
    tox_environments = [line for line in tox_environments if line not in ['clean', 'report', 'docs', 'check']]

    template_vars = defaultdict(list)
    template_vars['tox_environments'] = tox_environments
    for env in tox_environments:
        first, _ = env.split('-', 1)
        template_vars['%s_environments' % first].append(env)

    for name in os.listdir(join("ci", "templates")):
        with open(join(base_path, name), "w") as fh:
            fh.write('# NOTE: this file is auto-generated via ci/bootstrap.py (ci/templates/%s).\n' % name)
            fh.write(jinja.get_template(name).render(**template_vars))
        print(f"Wrote {name}")
    print("DONE.")


if __name__ == "__main__":
    args = sys.argv[1:]
    if args == ["--no-env"]:
        main()
    elif not args:
        exec_in_env()
    else:
        print(f"Unexpected arguments {args}", file=sys.stderr)
        sys.exit(1)
