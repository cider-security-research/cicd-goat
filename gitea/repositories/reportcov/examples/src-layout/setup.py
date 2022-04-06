from setuptools import find_packages
from setuptools import setup

setup(
    name='example',
    packages=find_packages('src'),
    package_dir={'': 'src'},
)
