import re
from setuptools import setup

version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('app/__init__.py').read(),
    re.M
    ).group(1)

with open("README.rst", "rb") as f:
    long_descr = f.read().decode("utf-8")

setup(name='app',
      description='Description for app',
      entry_points = {
        'console_scripts': ['app=app.main:main']
        },
      url='https://github.com/njfix6/py-efs-mounter',
      author='Nicholas Fix',
      author_email='njfix6@gmail.com',
      packages=['app'],
      long_description = long_descr,
      version=version
)
