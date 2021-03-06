from os.path import dirname, join

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def read(filename):
    with open(join(dirname(__file__), filename)) as f:
        return f.read()


_name = "demiconvert"
_license = "MIT"


setup(
    name=_name,
    description="A small unit conversion program",
    long_description=read("README.md"),
    version="0.1",
    license=_license,
    url="https://github.com/mikar/{}".format(_name),
    author="Max Demian",
    author_email="mikar@gmx.de",
    packages=[_name],
    package_data={_name: ["icon.png"]},
    install_package_data=True,
    entry_points={
                  "console_scripts": [
                      "{0} = {0}.cli:main".format(_name),
                  ],
                  "gui_scripts": [
                      "{0}-ui = {0}.gui:main".format(_name),
                  ],
              }
)
