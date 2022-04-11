"""
Flask-Meld
--------------
A way to meld your frontend and backend code
"""
import pathlib
from setuptools import setup

with open("flask_meld/__init__.py", "r") as f:
    version = [
        line.split(" = ")[1].strip()
        for line in f.readlines()
        if line.startswith("__version__")
    ][0].strip('"')

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

setup(
    name="Flask-Meld",
    version=version,
    url="http://github.com/mikeabrahamsen/Flask-Meld/",
    license="MIT",
    author="Michael Abrahamsen",
    author_email="mail@michaelabrahamsen.com",
    description="Meld is a framework for Flask that allows you to create dynamic user interfaces using Python and the Jinja2 templating engine.",
    long_description=README,
    long_description_content_type="text/markdown",
    packages=["flask_meld"],
    zip_safe=False,
    include_package_data=True,
    platforms="any",
    install_requires=[
        "Flask>=0.9",
        "beautifulsoup4>=4",
        "orjson>=3.4.6",
        "flask-socketio>=5",
        "gevent-websocket>=0.10.1",
        "jinja2-simple-tags==0.3.1",
        "click==7.1.2"
    ],
    tests_require=["pytest"],
    test_suite="tests",
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
